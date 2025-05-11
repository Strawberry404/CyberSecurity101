import streamlit as st

st.title("Common Cyber Attacks 🚨")

ATTACKS = {
    "Phishing": {
        "definition": "Deceptive emails or messages that trick users into revealing sensitive info.",
        "how_it_works": [
            "Attacker crafts a legitimate-looking email.",
            "Victim clicks link → fake login page.",
            "Credentials captured and reused."
        ],
        "mitigation": [
            "User training & simulated phishing drills.",
            "Email filtering, DMARC/SPF records.",
            "Multi-factor authentication."
        ],
        "image": "assets/images/phishing.png"
    },
    "Malware": {
        "definition": "Malicious software designed to damage or gain unauthorised access.",
        "how_it_works": [
            "Delivered via email, drive-by download, USB, etc.",
            "Installs itself, often with elevated privileges.",
            "Performs payload (spy, encrypt, destroy)."
        ],
        "mitigation": [
            "Up-to-date endpoint protection.",
            "Patch management, least-privilege.",
            "User awareness of suspicious files."
        ],
        "image": "assets/images/malware.png"
    },
    "DoS / DDoS": { ... },
    "SQL Injection": { ... },
    "Man-in-the-Middle": { ... },
    # add more...
}

attack_name = st.sidebar.selectbox("Select an attack", sorted(ATTACKS.keys()))
data = ATTACKS[attack_name]

st.subheader(attack_name)
st.image(data["image"], use_column_width=True)
st.markdown(f"**Definition:** {data['definition']}")

with st.expander("🧩 How it works"):
    st.write("\n".join(f"- {step}" for step in data["how_it_works"]))

with st.expander("🛡️ Mitigation"):
    st.write("\n".join(f"- {m}" for m in data["mitigation"]))
