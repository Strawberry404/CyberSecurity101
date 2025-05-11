# app.py
import streamlit as st
from pathlib import Path
import re, urllib.parse

# ── Configuration ─────────────────────────────────────────────
st.set_page_config(
    page_title="Cyber‑Attack Library",
    page_icon="🚨",
    layout="wide"
)

BASE_DIR    = Path(__file__).parent
ATTACKS_DIR = BASE_DIR / "attacks"           # folder with your .md files
N_COLS      = 3                              # cards per row on index page

# ── Helpers ───────────────────────────────────────────────────

def pretty(txt: str) -> str:                 # filename → human title
    return re.sub(r"[_\-]+", " ", txt).strip().title()

def slugify(txt: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")

# ── Scan markdown files once ─────────────────────────────────
files  = sorted(ATTACKS_DIR.glob("*.md"))
titles = [pretty(f.stem) for f in files]
slugs  = [slugify(t) for t in titles]

slug2path  = dict(zip(slugs, files))
slug2title = dict(zip(slugs, titles))

# ── Read current ?doc=… from URL (new API) ───────────────────
slug = st.query_params.get("doc")            # None if key absent

# ╭──────────────────────────────────────────────────────────╮
# │ Markdown renderer that also shows local images          │
# ╰──────────────────────────────────────────────────────────╯

def show_markdown_with_images(md_path: Path) -> None:
    """Render markdown and display local images referenced with ![alt](src)."""
    md_text = md_path.read_text(encoding="utf-8")

    # Split on markup pattern ![alt](src)
    pattern = r'!\[(.*?)\]\((.*?)\)'
    parts   = re.split(pattern, md_text)
    it      = iter(parts)

    for chunk in it:
        if chunk.strip():                    # avoid empty strings
            st.markdown(chunk)
        try:
            alt = next(it)                  # alt text
            src = next(it)                  # image path
        except StopIteration:
            break

        # ── Resolve the image path ──────────────────────────
        if src.startswith("app/static/"):
            img_path = BASE_DIR / src.replace("app/", "")
        elif src.startswith("static/"):
            img_path = BASE_DIR / src
        else:                                # relative to the .md file
            img_path = (md_path.parent / src)
        img_path = img_path.resolve()

        if img_path.exists():
            st.image(img_path, caption=alt, use_container_width=True)
        else:
            st.warning(f"Image not found: {src}")

# ╭──────────────────────────────────────────────────────────╮
# │ A) DETAIL PAGE                                          │
# ╰──────────────────────────────────────────────────────────╯
if slug and slug in slug2path:
    title = slug2title[slug]

    # Sidebar navigation
    st.sidebar.title("📚 Attack Index")
    choice = st.sidebar.radio("Jump to:", titles, index=titles.index(title))
    if choice != title:
        st.query_params["doc"] = slugs[titles.index(choice)]
        st.rerun()

    # Main content
    st.title(f"🚨 {title}")
    show_markdown_with_images(slug2path[slug])

    # Back button
    if st.button("⬅️ Back to list"):
        st.query_params.clear()
        st.rerun()

# ╭──────────────────────────────────────────────────────────╮
# │ B) INDEX / DASHBOARD PAGE                               │
# ╰──────────────────────────────────────────────────────────╯
else:
    # ── Sidebar hyperlinks to markdown details ─────────────
    st.sidebar.title("📚 Attack Index")
    for t, s in zip(titles, slugs):
        st.sidebar.markdown(f"- [{t}](?doc={urllib.parse.quote(s)})")

    # ── Main dashboard with prevention + attack catalogue ──
    st.title("🚨 Cybersecurity Overview")

    # ── Section: What we need to prevent ───────────────────
    with st.expander("🛡️ What Do We Need to Prevent?", expanded=True):
        st.markdown("""
- **Stealing users' accounts**  
- **Access to admin accounts**  
- **Exposure of sensitive information** (tutors, users, kids, parents)  
- **Shutting down the entire website**  
- **Redirecting users to malicious websites**  
- **Sending fake or spoofed emails**  
- **Integrating malicious advertising (malvertising)**  
- **Credential leakage**  
        """)

    # ── Section: Catalogue of attacks ──────────────────────
    with st.expander("🕷️ Types of Attacks We Need to Tackle", expanded=True):
        st.subheader("🔐 Authentication & Access")
        st.markdown("""
- [User enumeration](?doc=22-user-enumeration)  
- [Password mismanagement](?doc=13-password-mismanagement)  
- [Privilege escalation](?doc=15-privelage-escalation)  
- [Session fixation](?doc=18-session-fixation) / [Weak session IDs](?doc=weak-session-ids)  
- [Broken access control](?doc=2-broken-acces-control)  
- [Clickjacking](?doc=3-clickjacking) *(scaling threat)*  
        """)

        st.subheader("🧠 Injection & Execution Attacks")
        st.markdown("""
- [SQL injection](?doc=19-sql-injection)  
- [Regex injection](?doc=16-regex-injection)  
- [Cross‑Site Scripting](?doc=4-cross-site-scripting) (reflected, DOM, etc.)  
- [Host header poisoning](?doc=10-host-header-poisonning)  
        """)

        st.subheader("📦 Design & Dependency Risks")
        st.markdown("""
- [Insecure design](?doc=12-insecure-design)  
- [Toxic dependencies](?doc=21-toxic-dependecies)  
        """)

        st.subheader("🛰️ Network & Server‑Side Attacks")
        st.markdown("""
- [DNS poisoning](?doc=9-dns-poisoning)  
- [SSL stripping](?doc=20-ssl-stripting)  
- [Unencrypted communication](?doc=21-unencrypted-communication)  
- [Denial of Service](?doc=7-denial-of-service-attack)  
        """)

        st.subheader("📁 File & Client‑Side Risks")
        st.markdown("""
- [Directory traversal](?doc=8-directory-traversal)  
- [Cross‑Site Request Forgery](?doc=5-cross-site-request-forgery-csrf)  
        """)

        st.subheader("🛠️ Other & Scaling Concerns")
        st.markdown("""
- [Security misconfiguration](?doc=17-security-misconfiguration)  
- [Information leakage](?doc=11-information-leakage)  
- Logging & monitoring *(upcoming)*  
- Lax security settings  
- Subdomain squatting *(Upcoming)*
- Migration‑related integrations  
- Malvertising
        """)

        # ── Button grid for full list of available docs ────
        st.markdown("\n### 📑 Full Attack Library")
        cols = st.columns(N_COLS)
        for i, (t, s) in enumerate(zip(titles, slugs)):
            with cols[i % N_COLS]:
                if st.button(t, key=f"grid-{s}"):
                    st.query_params["doc"] = s
                    st.rerun()

    st.markdown("---")
    st.caption("© 2025 Your Name – Intro to Cybersecurity Demo")
