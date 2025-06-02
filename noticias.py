import feedparser

# 🌎 Lista de feeds RSS de notícias ambientais
feeds = [
     "https://www.gazetadopovo.com.br/rss/",
    "https://rss.feedspot.com/brazil_rss_feeds/",
    "https://rss.feedspot.com/brazil_rss_feeds/",
    "https://rss.dw.com/xml/rss_en_environment",
    "https://rss.dw.com/xml/rss_en_science",
    "https://rss.dw.com/rdf/rss-en-all",
    "https://www.affde.com/pt/top-world-news-websites-and-rss-feeds.html",
    "https://www.nationalgeographic.com/environment/rss.xml",
    "https://www.sciencedaily.com/rss/environment.xml",
    "https://www.wwf.org.br/rss.xml",
    "https://www.reuters.com/rssFeed",
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://www.theguardian.com/international/rss",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://www.bbc.co.uk/news/10628494"
]

def coletar_noticias():
    noticias = []
    
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        
        print(f"🔍 Processando {feed_url} - {len(feed.entries)} notícias encontradas")  # Debug

        for entrada in feed.entries[:10]:  # Pegando 10 notícias por feed
            titulo = entrada.title
            link = entrada.link
            
            print(f"🔹 Manchete encontrada: {titulo}")  # Exibir todas as manchetes
            
            # **Sem filtro** → Captura todas as notícias
            noticias.append(f"{titulo} - {link}")

    return noticias

# Salvar manchetes no arquivo
with open("manchetes.txt", "w", encoding="utf-8") as f:
    for noticia in coletar_noticias():
        f.write(noticia + "\n")

print("✅ Arquivo 'manchetes.txt' atualizado com todas as notícias coletadas!")



 
