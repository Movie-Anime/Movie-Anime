import os

def generate_info_md(title, genre, category, link1, link2=None):
    return f"""# {title}

**Genre:** {genre}  
**Kategori:** {category}  

📖 Deskripsi singkat tentang **{title}**, salah satu {category} terbaik dalam genre **{genre}**.

## 🔗 Link Unduhan
- [{link1}]({link1})
{"- [" + link2 + "](" + link2 + ")" if link2 else ""}

## 🔍 SEO Keywords
{title}, download {title}, {category} {genre}, streaming {title}, nonton {title} sub indo
"""

def add_new_title(base_path, category, genre, title, link1, link2=None):
    genre_path = os.path.join(base_path, category, genre)
    title_path = os.path.join(genre_path, title)
    os.makedirs(title_path, exist_ok=True)
    info_path = os.path.join(title_path, "info.md")
    with open(info_path, "w", encoding="utf-8") as f:
        f.write(generate_info_md(title, genre, category, link1, link2))

    # Tambah ke README.md genre
    readme_path = os.path.join(genre_path, "README.md")
    link_line = f"- [{title}](./{title.replace(' ', '%20')}/info.md)"
    if os.path.exists(readme_path):
        with open(readme_path, "r+", encoding="utf-8") as f:
            content = f.read()
            if link_line not in content:
                f.write(f"\n{link_line}\n")
    else:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# 📂 {genre} - {category} Collection\n\n")
            f.write("## 📺 Daftar Judul\n")
            f.write(link_line + "\n")

if __name__ == "__main__":
    base = "Movie-Anime"
    print("=== Tambah Judul Baru ===")
    category = input("Kategori (Film/Anime): ").strip()
    genre = input("Genre: ").strip()
    title = input("Judul: ").strip()
    link1 = input("Link unduhan 1: ").strip()
    link2 = input("Link unduhan 2 (opsional): ").strip()
    link2 = link2 if link2 else None

    add_new_title(base, category, genre, title, link1, link2)
    print(f"✅ Judul '{title}' telah ditambahkan ke {category}/{genre}/")