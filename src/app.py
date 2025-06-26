import streamlit as st
import requests
from datetime import datetime

API_KEY = st.secrets["API_KEY"]

@st.cache_data(ttl=3600)
def fetch_sources():
    url    = "https://newsapi.org/v2/sources"
    params = {"apiKey": API_KEY, "language": "en"}
    r      = requests.get(url, params=params)
    if r.status_code == 200:
        return sorted([(s["id"], s["name"]) for s in r.json()["sources"]],
                      key=lambda x: x[1])
    else:
        return []

def fetch_news(category, query, sources):
    url    = "https://newsapi.org/v2/top-headlines"
    params = {"apiKey": API_KEY}
    if sources:
        params["sources"] = ",".join(sources)
    else:
        params["category"] = category
    if query:
        params["q"] = query

    r = requests.get(url, params=params)
    if r.status_code == 200:
        return r.json().get("articles", [])
    else:
        st.error(f"NewsAPI error {r.status_code}: {r.text}")
        return []

def display_news(articles):
    for art in articles:
        pub = art.get("publishedAt")
        if pub:
            try:
                dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
                st.caption(f"🕒 {dt.strftime('%Y-%m-%d %H:%M:%S')}")
            except Exception:
                st.caption(f"🕒 {pub}")

        st.subheader(art["title"])
        st.write(art.get("description", ""))
        if art.get("urlToImage"):
            st.image(art["urlToImage"], use_container_width=True)
        st.write(f"[Read more]({art['url']})")
        st.markdown("---")

def main():
    st.title("🌐 News Explorer")

    # ─── show current datetime ────────────────────────────────────────────────
    now = datetime.now()
    st.write(f"**As of** {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # ─── sidebar controls ─────────────────────────────────────────────────────
    st.sidebar.header("Filters")
    category = st.sidebar.selectbox(
        "Category",
        ["business","entertainment","general","health","science","sports","technology"],
        index=2
    )
    query = st.sidebar.text_input("Keyword search")

    all_sources = fetch_sources()
    sources = st.sidebar.multiselect(
        "Sources (overrides category)",
        options=[s[0] for s in all_sources],
        format_func=lambda id: dict(all_sources)[id]
    )

    # ─── initialize on first load ─────────────────────────────────────────────
    if "articles" not in st.session_state:
        st.session_state.articles = fetch_news(category, query, sources)

    # ─── re-fetch on demand ────────────────────────────────────────────────────
    if st.sidebar.button("Get News"):
        st.session_state.articles = fetch_news(category, query, sources)

    # ─── display ───────────────────────────────────────────────────────────────
    if st.session_state.articles:
        display_news(st.session_state.articles)
    else:
        st.info("No articles found for those filters.")

if __name__ == "__main__":
    main()
