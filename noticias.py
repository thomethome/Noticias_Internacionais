import feedparser

# URLs de feeds de notícias internacionais
feeds = [
    "http://rss.cnn.com/rss/edition_world.rss",
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

def coletar_noticias():
    noticias = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entrada in feed.entries[:5]:  # Pegando as 5 últimas notícias
            titulo = entrada.title
            link = entrada.link
            noticias.append(f"{titulo} - {link}")

    return noticias

# Salvar manchetes no arquivo
with open("manchetes.txt", "w", encoding="utf-8") as f:
    for noticia in coletar_noticias():
        f.write(noticia + "\n")

print("✅ Arquivo 'manchetes.txt' atualizado com notícias internacionais!")
 
