import streamlit as st
from pathlib import Path
import re, urllib.parse

# ── Configuration ─────────────────────────────────────────────
st.set_page_config(page_title="Cyber-Attack Library", page_icon="🚨", layout="wide")
ATTACKS_DIR = Path(__file__).parent / "attacks"   # folder with your .md files
N_COLS = 3                                        # cards per row on index page

# ── Helpers ───────────────────────────────────────────────────
def pretty(txt: str) -> str:   # filename → human title
    return re.sub(r"[_\-]+", " ", txt).strip().title()

def slugify(txt: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")

# ── Scan markdown files once ─────────────────────────────────
files   = sorted(ATTACKS_DIR.glob("*.md"))
titles  = [pretty(f.stem) for f in files]
slugs   = [slugify(t) for t in titles]
slug2path  = dict(zip(slugs, files))
slug2title = dict(zip(slugs, titles))

# ── Read current ?doc=… from URL via **new API** ─────────────
slug = st.query_params.get("doc")        # returns None if key absent

# ──────────────────────────────────────────────────────────────
#  A) DETAIL PAGE
# ──────────────────────────────────────────────────────────────
if slug and slug in slug2path:
    title   = slug2title[slug]
    content = slug2path[slug].read_text(encoding="utf-8")

    # Sidebar: jump directly to another attack
    st.sidebar.title("📚 Attack Index")
    choice = st.sidebar.radio("Jump to:", titles, index=titles.index(title))
    if choice != title:                            # user picked another item
        st.query_params["doc"] = slugs[titles.index(choice)]
        st.rerun()

    # Main area
    st.title(f"🚨 {title}")
    st.markdown(content, unsafe_allow_html=True)

    # Back button → clear query params
    if st.button("⬅️ Back to list"):
        st.query_params.clear()
        st.rerun()

# ──────────────────────────────────────────────────────────────
#  B) INDEX PAGE
# ──────────────────────────────────────────────────────────────
else:
    # Sidebar list with hyperlinks
    st.sidebar.title("📚 Attack Index")
    for t, s in zip(titles, slugs):
        st.sidebar.markdown(f"- [{t}](?doc={urllib.parse.quote(s)})")

    # Cards on the main page
    st.title("🚨 Common Cyber-Attacks")
    cols = st.columns(N_COLS)
    for i, (t, s) in enumerate(zip(titles, slugs)):
        with cols[i % N_COLS]:
            if st.button(t, key=s):
                st.query_params["doc"] = s        # set param
                st.rerun()

    st.markdown("---")
    st.caption("© 2025 Your Name – Intro to Cybersecurity Demo")
