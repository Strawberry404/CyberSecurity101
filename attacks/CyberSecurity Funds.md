
# Cyber-Security Fundamentals 🚀  
*(In-depth reference — 2025 edition)*  

---

## 1  The CIA**A** Triad  

| Pillar                            | What It Protects                             | Why It Fails                                      | Canonical Controls                                                                                   |
| --------------------------------- | -------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Confidentiality**               | Secrets, PII, trade secrets                  | credential reuse, sniffed plaintext, side-channel | TLS 1.3 everywhere, envelope encryption (KMS), attribute-based access control (ABAC), DLP, VPN, NDAs |
| **Integrity**                     | Correctness & non-repudiation of data & code | injection, on-path tampering, supply-chain        | HMAC-SHA-256, signed commits (Sigstore / cosign), TPM-measured boot, immutability in S3+Object Lock  |
| **Availability**                  | Service uptime & timely access               | DDoS, ransomware, cloud mis-quota, BGP hijack     | autoscaling, WAF/CDN, multi-AZ/region, anycast scrubbing, immutable backups (3-2-1-1-0)              |
| **Authenticity / Accountability** | Proof of identity *and* attribution          | password theft, session hijack, log deletion      | FIDO2/WebAuthn, device posture, MACsec, tamper-proof logging (WORM, blockchain), SIEM-to-SOAR        |

> 💡 **Remember:** CIAA ↔ *“Can I Access Auth?”*.  
> In exam essays, link each pillar to 2-3 concrete controls.

---

## 2  Threat Landscape  

### 2.1  Passive vs. Active  

| Mode | Core Goal | Common Vectors | Hard Countermeasures |
|------|-----------|----------------|----------------------|
| **Passive** | Surreptitious intel | 802.11 monitor mode, fibre taps, EM emissions (TEMPEST) | end-to-end encryption, Wi-Fi 6E WPA3-SAE, Faraday cage, OS hardening (`sysctl kernel.randomize_va_space=2`) |
| **Active** | Alter / disrupt | MITM, privilege escalation, Wiper malware, route injection | mutual auth, SELinux confines, kernel lockdown, signed config (gitops), secure BGP (RPKI) |

### 2.2  Attack Classes + Defenses

| Class | Kill-Chain Phases (<abbr title="MITRE ATT&CK">ATT&amp;CK</abbr>) | Deeper Examples | Layered Defenses |
|-------|----------------|----------------|-----------------|
| **Reconnaissance** | TA0043 (Acquire Infra) → TA0042 (Resource Dev) | certificate transparency scraping, GitHub dorking, cloud-asset search (Censys) | external attack-surface Mgmt (EASM), `robots.txt` honeypots, canary subdomains |
| **Injection** | Initial Access & Priv-Esc | GraphQL ID injection, LDAP filter, XXE, SSTI (Jinja2 `{{ 7*7 }}`) | allow-list parsers, zero-copy parameter binding (`$1`), WAF with token replay defence, `seccomp-bpf` |
| **Flooding** | Impact (TA0040) | HTTP/2 Reset flood (2023 CVE-2023-44487), amplification via memcached UDP, carpet-bombing | Cloudflare Magic Transit, SYN cookies (`ISN = hash(src,dst,tcpopts) << 24 | MSS`), adaptive L4 rate-limiter |
| **Spoofing** | Credential Access | Bit-Blt token swap, NTLM relay, STUN/IP spoof for reflection | DKIM/DMARC alignment, SMB signing, mTLS with SAN pinning, ingress-egress filter (RFC 3704) |
| **Logic Abuse** | Priv-Esc & Execution | insecure direct object reference (IDOR), numeric overflow in loyalty points, TOTP replay | domain-driven access checks, BFF-pattern APIs, anti-replay nonce db, 4-eyes approval |
| **Malware** | Execution & Impact | double-ext `invoice.pdf.exe`, `mshta` LOLBin, on-chain ransomware payment automation | LAPS, JEA, EDR with kernel sensor, YARA rules, air-gapped backups |
| **Supply-Chain** | Persistence & Priv-Esc | malicious PyPI `pymafka`, XZ backdoor (CVE-2024-3094), IDE plugin trojan | SBOM (CycloneDX), SLSA Level 3+, dist-sig (sigstore), dependency track, reproducible builds |
| **Side-Channel / Downgrade** | Collection | ROBOT (Bleichenbacher), Lucky13, Wi-Fi Kr00k, screen emissions (Van Eck) | constant-time code, AEAD only, HSTS pre-load, microcode updates, EM shielding |
| **Config / Human** | Initial Access | GitLab runner with wildcard `--privileged`, Slack token in README, mis-set CORS `*` | IaC scanning (tfsec), secrets vault, push-protect (GH Secret Scanning), PASTA threat-modeling |

---

## 3  Network Attacks in Depth  

### 3.1  SYN Flood — internal maths  

TCP server alloc allocates `sk_buff` per `SYN`. When backlog `N` ≈ `tcp_max_syn_backlog`, new handshakes dropped ⇒ DoS.  

**SYN cookies algorithm** *(RFC 4987)*:  

```

ISN = t << 24 | MSS_index << 21 | hash(srcIP, dstIP, srcPort, dstPort, secret, t) & 0x7FFFFF

```

Server therefore stores **no state** until it receives ACK with the cookie in seq + 1.

### 3.2  IP Spoofing Detection  

* **TTL analysis** — forged packets often have atypical TTL vs. legit baseline.  
* **Hop-Count Filtering (HCF)** — map IP → expected hop-count; drop anomalies.  
* **uRPF (strict)** on routers (`ip verify source reachable-via rx`) = egress BCP 38.

### 3.3  Proxy Chains & VPN — traffic flow diagram  

```

Client ─TLS──► Forward-Proxy (:3128) ─TLS──► Tor-Guard ─TLS──► Target  
Client ─WG──► WireGuard Tunnel (UDP/51820) ─► Corp-LAN

```

> **Split-tunnel**: only `10.0.0.0/8,172.16.0.0/12,192.168.0.0/16` go via VPN; rest via ISP.

### 3.4  DMZ Architecture (3-tier)  

```

```
      Internet
          │
    [Edge FW / WAF]
          │
     ┌─────────┐
     │  DMZ    │  ← reverse-proxy, mail-relay, honeypot
     └─────────┘
          │ (stateful FW)
     ┌─────────┐
     │  APP    │  ← app servers, API BFF
     └─────────┘
          │ (DB-FW)         outbound-only
     ┌─────────┐  ─────►  S3 / Updates
     │  DATA   │
     └─────────┘
```

```

### 3.5  Honeypot Telemetry  

*Low-interaction* (e.g. **T-Pot**) harvests credential dictionaries & new C2 IPs.  
*High-interaction* (e.g. full Windows 10 VM) records attacker behaviour via **QEMU-KVM snapshot differencing**; revert after compromise.

---

## 4  Cryptography Corner  

### 4.1  TLS 1.3 Handshake — wire view  

| Msg | Dir | Key Material |
|-----|-----|--------------|
| ClientHello | ➡ | client_random, keyshare(X25519) |
| ServerHello | ⬅ | server_random, keyshare, selects cipher |
| EncryptedExtensions + Certificate + CertVerify | ⬅ | encrypted with handshake_secret |
| Finished | ⬅ | verifies server handshake |
| Finished | ➡ | verifies client handshake |

All subsequent records encrypted with `traffic_secret = HKDF-Expand(master_secret, …)`

### 4.2  RSA Keygen Math  

1. Choose 2 primes `p ≈ q` (2048 bit total).  
2. `n = p*q`,  φ(n)= (p−1)(q−1).  
3. Select `e` coprime to φ(n) (65537).  
4. Compute `d = e⁻¹ mod φ(n)`.  
5. Public key = `(e,n)`; private = `(d,n)`.  
6. Signature: `s = H(m)^d mod n`. Verify `s^e mod n == H(m)`.

### 4.3  ECDSA Math (P-256)  

*Curve*: `y² = x³ − 3x + b` over prime `p`.  
*Sign*: choose nonce `k`, compute `(x₁,y₁)=kG`, `r = x₁ mod n`, `s = k⁻¹(H(m)+rd) mod n`.  
*Verify*: `(u₁,u₂)=(H(m)s⁻¹, rs⁻¹)`, point `P = u₁G + u₂Q`; valid if `P.x mod n == r`.

> **Nonce reuse leaks `d`**. Use RFC 6979 deterministic `k`.

### 4.4  Post-Quantum Preview  

* **KEM**: CRYSTALS-Kyber CLS-L3 (key = 1184 B, Ct = 1088 B, IND-CCA).  
* **Sig**: Dilithium (L3). Hybrid TLS (`x25519+kyber768`, `ecdsa_p256+dilithium3`) already in Chrome/Firebase (2024).

---

## 5  IPC vs. VPN — deeper  

| Topic | IPC | VPN |
|-------|-----|-----|
| Packet Boundary | None (byte-stream) or app msg | preserved IP/UDP packets |
| Threats | race, shmem leak, TOCTOU, priority inversion | MITM, DNS leak, routing loop, split-tunnel exfil |
| Hardening | SELinux type-enforce, `memfd` sealed, seccomp | perfect-forward secrecy, MSS clamping, kill-switch, IPv6 leak-block |

---

## 6  Legal & Regulatory — exam deep-dive points  

### Morocco (Law 09-08, 07-03, 05-20)  

* CNDP = **Commission Nationale de Contrôle de la Protection des Données**.  
* Max fine: 300 000 MAD &/or 2 years prison for unlawful processing.  
* 2024 draft “Cyber-security & Critical Infrastructure Act” imposes NIS-like incident reporting (< 72 h).

### USA (CFAA, CIRCIA 2024)  

* **CFAA §1030**: “unauthorised access” controversies (Van Buren v. US 2021).  
* **CIRCIA**: critical infra must report “substantial cyber incidents” to CISA within 72 h; ransom payments within 24 h. Civil penalties up to \$50 000/day.

### EU (NIS2, CRA)  

* **NIS2**: scope ↔ 18 sectors (Annex I+II), fines = €10 M / 2 % revenue.  
* **Cyber-Resilience Act**: mandatory SBOM, 24 h “actively exploited vuln” patch release, 3 vendor classes.

---

## 7  Defence-in-Depth Stack — tooling examples  

| Stage | Representative Tools |
|-------|---------------------|
| Identify | **CMDB** (ServiceNow), **Cartography**, **Shodan Search Monitor** |
| Protect | AWS GuardDuty, Azure Defender, Kubernetes PodSecurity, **OPA/Gatekeeper** |
| Detect | **Sigma** rules → **Elastic SIEM**, **Falco** (K8s runtime), Zeek IDS |
| Respond | **SOAR** (Cortex XSOAR), IR runbooks (Jupyter IR), Slack / Mattermost bots |
| Recover | Immutable EBS+ReFS, DRaaS, tabletop via **Chaos Slinger** |

---

## 8  Future Focus — nuanced risks  

1. **PQ-Hybrid tech-debt** — need dual-stack cipher agility (TLS 1.3 + pqc-kem).  
2. **Adversarial LLMs** — jail-breaks to auto-craft spear-phish; defenders deploy **AI-RED TEAM**.  
3. **MFA fatigue bypass** — push-phish replaced by **passkey↔device attestation**.  
4. **5G & Edge-Compute** — micro-slices → new lateral movement paths, require micro-segmentation (SASE).  
5. **Climate DoS** — extreme weather outages; multi-continent edge caching a must (BCM).

---

### Quick Glossary (v2)  

| Term | 2-line Elevator Pitch |
|------|----------------------|
| **RPKI** | BGP route-origin validation; cryptographically signs which ASN may announce a prefix. |
| **HSTS** | Header (`Strict-Transport-Security`) forces HTTPS; stops SSL-strip. |
| **SLSA** | Supply-chain Levels for Software Artifacts (v1.0) — provenance attestation; SLSA 4 = hermetic + 2-party review. |
| **Anycast** | Same IP announced by many POPs; nearest node absorbs traffic, handy for DDoS. |
| **Chaos-Engineering** | Intentionally break prod to prove resilience; pioneered by Netflix *Chaos Monkey*. |

---

© 2025 Cyber-Attack Library · CC-BY-SA 4.0  