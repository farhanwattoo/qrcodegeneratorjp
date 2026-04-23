import os
import re

PAGES = [
    {"slug": "qr-code-generator", "keyword": "QRコード 作成", "secondary": "QRコード 無料, QRコード 作り方", "intent": "Tool", "desc": "Main generator", "type": "Core"},
    {"slug": "free-qr-code-generator", "keyword": "QRコード 無料", "secondary": "無料 QRコード 作成", "intent": "Tool", "desc": "No signup", "type": "Core"},
    {"slug": "qr-code-online", "keyword": "QRコード オンライン", "secondary": "QRコード 作成 サイト", "intent": "Tool", "desc": "Fast load", "type": "Core"},
    {"slug": "wifi-qr-code", "keyword": "WiFi QRコード 作成", "secondary": "wifi qr 作り方", "intent": "Tool", "desc": "SSID + password", "type": "Type"},
    {"slug": "line-qr-code", "keyword": "LINE QRコード 作成", "secondary": "line qrコード 作り方", "intent": "Tool", "desc": "VERY IMPORTANT", "type": "Type"},
    {"slug": "url-qr-code", "keyword": "URL QRコード 作成", "secondary": "リンク QRコード", "intent": "Tool", "desc": "Website links", "type": "Type"},
    {"slug": "contact-qr-code", "keyword": "連絡先 QRコード", "secondary": "vcard qr", "intent": "Tool", "desc": "Save contact", "type": "Type"},
    {"slug": "email-qr-code", "keyword": "メール QRコード", "secondary": "email qr code", "intent": "Tool", "desc": "Email link", "type": "Type"},
    {"slug": "qr-code-for-menu", "keyword": "メニュー QRコード", "secondary": "レストラン qr", "intent": "Commercial", "desc": "Restaurant", "type": "Use Case"},
    {"slug": "qr-code-for-payment", "keyword": "決済 QRコード", "secondary": "支払い qrコード", "intent": "Commercial", "desc": "Payment use", "type": "Use Case"},
    {"slug": "qr-code-for-business-card", "keyword": "名刺 QRコード", "secondary": "ビジネスカード qr", "intent": "Commercial", "desc": "Networking", "type": "Use Case"},
    {"slug": "custom-qr-code", "keyword": "デザイン QRコード", "secondary": "カスタム qr", "intent": "Tool", "desc": "Design editor", "type": "Feature"},
    {"slug": "color-qr-code", "keyword": "カラー QRコード", "secondary": "色付き qr", "intent": "Tool", "desc": "Colors", "type": "Feature"},
    {"slug": "logo-qr-code", "keyword": "ロゴ QRコード", "secondary": "ロゴ入り qr", "intent": "Tool", "desc": "Branding", "type": "Feature"},
    {"slug": "qr-code-svg", "keyword": "QRコード SVG", "secondary": "ベクター qr", "intent": "Tool", "desc": "Download SVG", "type": "Format"},
    {"slug": "qr-code-png", "keyword": "QRコード PNG", "secondary": "qr png ダウンロード", "intent": "Tool", "desc": "Image export", "type": "Format"},
    {"slug": "qr-code-not-working", "keyword": "QRコード 読み取れない", "secondary": "qrコード エラー", "intent": "Info", "desc": "Fix guide", "type": "Problem"},
    {"slug": "qr-code-size", "keyword": "QRコード サイズ", "secondary": "qrコード 大きさ", "intent": "Info", "desc": "Size guide", "type": "Problem"},
    {"slug": "qr-code-for-restaurant", "keyword": "飲食店 QRコード", "secondary": "飲食 qr", "intent": "Programmatic", "desc": "飲食店向け", "type": "Programmatic"},
    {"slug": "qr-code-for-salon", "keyword": "美容室 QRコード", "secondary": "美容院 qr", "intent": "Programmatic", "desc": "美容室向け", "type": "Programmatic"},
    {"slug": "qr-code-for-gym", "keyword": "ジム QRコード", "secondary": "フィットネス qr", "intent": "Programmatic", "desc": "ジム向け", "type": "Programmatic"},
    {"slug": "qr-code-for-school", "keyword": "学校 QRコード", "secondary": "教育 qr", "intent": "Programmatic", "desc": "学校向け", "type": "Programmatic"},
    {"slug": "qr-code-for-real-estate", "keyword": "不動産 QRコード", "secondary": "物件 qr", "intent": "Programmatic", "desc": "不動産向け", "type": "Programmatic"},
    {"slug": "qr-code-for-hospital", "keyword": "病院 QRコード", "secondary": "クリニック qr", "intent": "Programmatic", "desc": "病院向け", "type": "Programmatic"}
]

BASE_URL = "https://qrcodegeneratorjp.com"
DIR = r"c:\Users\farhan.atif\Desktop\tools website\qrcodegeneratorjp-main"

def build_footer():
    html = ['<footer id="semantic-links" style="background: #f9fafb; padding: 3rem 1rem; margin-top: 4rem; border-top: 1px solid #e5e7eb;">']
    html.append('<div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">')
    
    groups = {}
    for p in PAGES:
        groups.setdefault(p["type"], []).append(p)
        
    for gtype, items in groups.items():
        html.append('<div>')
        html.append(f'<h4 style="font-size: 1rem; margin-bottom: 1rem; color: #111827;">{gtype}</h4>')
        html.append('<ul style="list-style: none; padding: 0; margin: 0; line-height: 1.8; font-size: 0.9rem;">')
        for item in items:
            html.append(f'<li><a href="/{item["slug"]}.html" style="color: #4b5563; text-decoration: none;">{item["keyword"]}</a></li>')
        html.append('</ul>')
        html.append('</div>')

    html.append('</div>')
    html.append(f'<div style="max-width: 1200px; margin: 2rem auto 0; text-align: center; font-size: 0.85rem; color: #6b7280; border-top: 1px solid #e5e7eb; padding-top: 2rem;">&copy; 2026 QR Generator Online. All rights reserved. | <a href="/sitemap.xml" style="color: #4b5563; text-decoration: none;">Sitemap</a></div>')
    html.append('</footer>')
    return "\n".join(html)

def build_content_section(page, all_pages):
    keyword = page["keyword"]
    secondary = page["secondary"]
    intent = page["intent"]
    ptype = page["type"]
    
    html = []
    html.append('<section class="content-section">')
    
    if ptype == "Core":
        html.append(f'<h2>{keyword}について（使い方と仕組み）</h2>')
        html.append(f'<p>当サイトは、PCやスマホからブラウザ上で完結する完全無料の{keyword}ツールです。「{secondary}」と検索して訪れた方にも最適なソリューションを提供します。アプリ不要で安全に生成可能です。近年、QRコードはオフラインとオンラインを繋ぐ重要な役割を果たしており、手軽に情報共有する手段として欠かせません。</p>')
    elif ptype == "Type":
        html.append(f'<h2>{keyword}の作り方と特徴</h2>')
        html.append(f'<p>{keyword}を作成することで、情報の共有が劇的にスムーズになります。「{secondary}」にお悩みの方でも、当ツールを使えば数秒で生成できます。複雑な設定は一切不要で、必要なデータを入力するだけで即座に高品質なQRコードが出力されます。</p>')
    elif ptype in ["Use Case", "Programmatic"]:
        html.append(f'<h2>ビジネス向け：{keyword}の活用法とメリット</h2>')
        html.append(f'<p>店舗や施設で{keyword}を導入することで、顧客満足度の向上や業務効率化が期待できます。「{secondary}」を探している事業者様にも完全無料で商用利用いただけます。チラシ、ポスター、名刺、またはウェブサイトなどに掲載することで、顧客を目的のページへスムーズに誘導でき、コンバージョン率の向上に直結します。</p>')
    elif ptype == "Feature":
        html.append(f'<h2>高度な設定：{keyword}機能について</h2>')
        html.append(f'<p>標準的なQRコードだけでなく、当サイトでは{keyword}にも対応しています。「{secondary}」としてブランド力アップやデザイン性向上に活用してください。カラー変更やサイズ調整を駆使することで、あなたのブランドイメージにぴったり合ったオリジナルデザインのQRコードを作成することが可能です。</p>')
    elif ptype == "Format":
        html.append(f'<h2>出力形式：{keyword}での保存・ダウンロード</h2>')
        html.append(f'<p>生成したQRコードは、用途に合わせて{keyword}でダウンロード可能です。「{secondary}」を求めるデザイナーや印刷業者様にも最適な高画質出力をサポートします。印刷物に使用する場合は、解像度やサイズが非常に重要になりますので、当ツールのサイズ変更機能を活用して最適なデータを出力してください。</p>')
    elif ptype == "Problem":
        html.append(f'<h2>トラブルシューティング：{keyword}の確実な解決策</h2>')
        html.append(f'<p>{keyword}に関するよくある問題と解決策を解説します。「{secondary}」でお困りの方は、以下のポイントを確認して再度生成をお試しください。多くの場合、コントラスト不足やサイズが小さすぎることが原因です。当ツールで再生成することで、確実に読み取れるQRコードを作成できます。</p>')
    else:
        html.append(f'<h2>{keyword}の詳細情報</h2>')
        html.append(f'<p>{keyword}（{secondary}）についての詳しい解説と使い方です。</p>')

    html.append(f'<h3 style="margin-top: 2rem;">{keyword}を作成する3つの簡単なステップ</h3>')
    html.append(f'<ol style="line-height: 1.8; margin-bottom: 2rem;">')
    html.append(f'<li><strong>情報の入力:</strong> 上部の入力フォームに目的のデータ（URLやテキストなど）を入力します。</li>')
    html.append(f'<li><strong>カスタマイズ:</strong> 必要に応じて色やサイズ、エラー訂正レベルを調整します。</li>')
    html.append(f'<li><strong>ダウンロード:</strong> 「QRコードをダウンロード (PNG)」ボタンをクリックして保存します。</li>')
    html.append(f'</ol>')

    # Internal Linking
    html.append('<h3>関連するQRコード作成ツール</h3>')
    html.append('<p>目的や用途に合わせて、以下の専用ツールも無料でご利用いただけます：</p>')
    html.append('<ul>')
    
    related = [p for p in all_pages if p["type"] == ptype and p["slug"] != page["slug"]]
    if len(related) < 4:
        related += [p for p in all_pages if p["type"] in ["Type", "Use Case", "Core"] and p["slug"] != page["slug"]]
    
    # Remove duplicates preserving order
    seen = set()
    related_unique = []
    for p in related:
        if p["slug"] not in seen:
            seen.add(p["slug"])
            related_unique.append(p)
            
    for rel_page in related_unique[:5]:
        html.append(f'<li><a href="/{rel_page["slug"]}.html" style="color: var(--primary); text-decoration: none; font-weight: 600;">{rel_page["keyword"]}</a> - {rel_page["desc"]}</li>')
    html.append('</ul>')
    
    # Dynamic FAQ based on Keyword
    html.append('<div class="faq" style="margin-top: 3rem;">')
    html.append('<h3>よくある質問 (FAQ)</h3>')
    
    html.append('<div class="faq-item">')
    html.append(f'<h4>{keyword}は無料で作成・商用利用できますか？</h4>')
    html.append(f'<p>はい、当サイトの{keyword}機能は完全無料です。個人利用から法人の商用利用（チラシ、ポスター、メニュー表、名刺への印刷など）まで制限なくお使いいただけます。</p>')
    html.append('</div>')
    
    html.append('<div class="faq-item">')
    html.append(f'<h4>{keyword}の有効期限や回数制限はありますか？</h4>')
    html.append(f'<p>生成された{keyword}自体に有効期限や読み取り回数の制限はありません。ただし、設定したURLやリンク先が削除された場合は読み取れなくなるためご注意ください。</p>')
    html.append('</div>')
    
    html.append('<div class="faq-item">')
    html.append(f'<h4>生成時のセキュリティやプライバシーはどうなっていますか？</h4>')
    html.append(f'<p>当ツールは入力データをサーバーへ送信せず、すべてお使いのブラウザ内部でQRコードを生成します。そのため、入力内容が外部に漏れることはなく極めて安全です。</p>')
    html.append('</div>')
    
    html.append('</div>')
    html.append('</section>')
    
    return "\n".join(html)

def generate():
    index_path = os.path.join(DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the existing footer
    footer_pattern = re.compile(r'<footer id="semantic-links".*?>.*?</footer>', re.DOTALL)
    new_footer = build_footer()
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(new_footer, content)
    else:
        # Just insert it before </div>\n    <!-- Script Injection Architecture -->
        content = content.replace("    <!-- Script Injection Architecture -->", new_footer + "\n    <!-- Script Injection Architecture -->")
    
    # Save the updated index.html
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    sitemap_urls = [f"{BASE_URL}/"]

    for page in PAGES:
        page_content = content
        
        # Meta replacements
        keyword = page['keyword']
        secondary = page['secondary']
        ptype = page['type']
        
        if ptype == "Core":
            title = f"{keyword}【完全無料】アプリ不要でブラウザから即時作成"
            desc = f"【商用利用OK】{keyword} ({secondary}) に最適な無料ツール。URL、テキスト、WiFiなどの情報を入力するだけで、安全かつ一瞬でQRコードを生成・ダウンロード可能です。"
        elif ptype == "Type":
            title = f"{keyword} | 無料で簡単・安全に生成するツール"
            desc = f"{keyword}をブラウザ上で簡単に作成できます。「{secondary}」をお探しの方へ。会員登録不要・商用フリーで、作成したQRコードはPNG形式で即座に保存可能です。"
        elif ptype in ["Use Case", "Programmatic"]:
            title = f"{keyword}を無料作成 | ビジネス・店舗の集客に最適"
            desc = f"店舗や施設での集客・業務効率化に役立つ【{keyword}】を完全無料で自動生成。商用利用可能でアプリは不要。「{secondary}」にも対応し、印刷物やWebですぐに使えます。"
        elif ptype == "Feature":
            title = f"{keyword}を簡単作成 | カスタマイズ可能な無料生成ツール"
            desc = f"デザイン性を高める【{keyword}】を作成できる無料ツール。「{secondary}」をお探しの方へ。色やサイズを自由にカスタマイズして、高品質なQRコードをダウンロードできます。"
        elif ptype == "Format":
            title = f"{keyword}で無料ダウンロード | 高画質なQRコード生成"
            desc = f"作成したQRコードを【{keyword}】でダウンロードできる無料ツールです。「{secondary}」で高解像度の画像が必要なクリエイターや印刷業者様に最適。商用利用も可能です。"
        elif ptype == "Problem":
            title = f"{keyword}の解決策と正しい作成方法ガイド"
            desc = f"【{keyword}】にお悩みの方へ。「{secondary}」の原因と、確実に読み取れるQRコードを無料で再作成・生成するためのガイドライン・対処法を提供します。"
        else:
            title = f"{keyword} | 無料で簡単作成・ダウンロード"
            desc = f"{keyword} ({secondary}) に対応したQRコード生成ツールです。アプリ不要で安全に作成でき、商用利用も可能です。"

        keywords = f"{keyword}, {secondary}, QRコード, 作成, 無料, ツール"
        
        page_content = re.sub(r'<title.*?>.*?</title>', f'<title id="meta-title">{title}</title>', page_content, count=1)
        page_content = re.sub(r'<meta id="meta-desc" name="description" content=".*?">', f'<meta id="meta-desc" name="description" content="{desc}">', page_content, count=1)
        page_content = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{keywords}">', page_content, count=1)
        
        page_content = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', page_content, count=1)
        page_content = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', page_content, count=1)
        
        page_content = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{title}">', page_content, count=1)
        page_content = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{desc}">', page_content, count=1)
        
        page_content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{BASE_URL}/{page["slug"]}.html">', page_content, count=1)
        page_content = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{BASE_URL}/{page["slug"]}.html">', page_content, count=1)

        # H1 & Hero Paragraph Replacement
        page_content = re.sub(r'<h1>.*?</h1>', f'<h1>{page["keyword"]}ツール</h1>', page_content, count=1)
        
        # Customize hero paragraph based on intent
        hero_p = f"このページでは「{page['keyword']}」を簡単・安全に作成できます。{page['secondary']}に対応した、インストール不要のウェブ版ツールです。商用利用可能で、カスタマイズやダウンロード（PNG/SVG）も手軽に行えます。"
        if page['type'] == 'Programmatic':
            hero_p = f"【{page['desc']}】店舗や施設で使える{page['keyword']}を簡単に作成できます。チラシ、メニュー表、店頭ポスターなどでの集客や利便性向上に役立ちます。完全無料で商用利用も可能です。"
            
        # The hero section structure in index.html is:
        # <section class="hero">
        #     <h1>...</h1>
        #     <p>...</p>
        # </section>
        # We need to replace the <p> exactly after <h1>.
        page_content = re.sub(r'(<section class="hero">\s*<h1>.*?</h1>\s*)<p>.*?</p>', rf'\1<p>{hero_p}</p>', page_content, count=1, flags=re.DOTALL)
        
        # Add dynamic ARIA Label to canvas
        page_content = re.sub(r'aria-label="Generated output format target"', f'aria-label="{keyword}のプレビュー画像"', page_content)

        # Inject Breadcrumbs Visually
        breadcrumb_html = f'''        <!-- BREADCRUMBS -->
        <nav class="breadcrumbs" aria-label="breadcrumb" style="margin-bottom: 1rem; font-size: 0.85rem; color: #6b7280;">
            <a href="/" style="color: #4f46e5; text-decoration: none; font-weight: 600;">ホーム</a> &gt; 
            <strong style="color: #111827;">{keyword}</strong>
        </nav>'''
        page_content = re.sub(r'(<section class="hero">)', breadcrumb_html + r'\n        \1', page_content, count=1)

        # Inject Dynamic JSON-LD Schema
        json_ld = f'''    <!-- Dynamic SEO Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{title}",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "All",
      "description": "{desc}",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "JPY"
      }}
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "ホーム",
          "item": "{BASE_URL}/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{keyword}",
          "item": "{BASE_URL}/{page['slug']}.html"
        }}
      ]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "{keyword}は無料で作成・商用利用できますか？",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "はい、当サイトの{keyword}機能は完全無料です。個人利用から法人の商用利用（チラシ、ポスター、メニュー表、名刺への印刷など）まで制限なくお使いいただけます。"
          }}
        }},
        {{
          "@type": "Question",
          "name": "{keyword}の有効期限や回数制限はありますか？",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "生成された{keyword}自体に有効期限や読み取り回数の制限はありません。ただし、設定したURLやリンク先が削除された場合は読み取れなくなるためご注意ください。"
          }}
        }}
      ]
    }}
    </script>'''
        
        # Replace existing static JSON-LD from index.html template
        page_content = re.sub(r'<!-- Essential Initial Schema Markup for Root -->.*?</script>\s*</head>', json_ld + '\n</head>', page_content, flags=re.DOTALL)
        
        
        # Replace Content Section for dynamic SEO and internal linking
        content_pattern = re.compile(r'<section class="content-section">.*?</section>', re.DOTALL)
        # Avoid substituting index.html contents when it is the index itself, wait, index.html is qr-code-generator.html equivalent, but we don't save index.html here, we only use it as template.
        # Actually, let's just replace it for all generated pages.
        new_content_section = build_content_section(page, PAGES)
        page_content = content_pattern.sub(new_content_section, page_content, count=1)
        
        # Write HTML
        page_path = os.path.join(DIR, f"{page['slug']}.html")
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(page_content)
            
        sitemap_urls.append(f"{BASE_URL}/{page['slug']}.html")
        
    # Generate sitemap.xml
    sitemap_path = os.path.join(DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in sitemap_urls:
            f.write('  <url>\n')
            f.write(f'    <loc>{url}</loc>\n')
            f.write('    <changefreq>weekly</changefreq>\n')
            f.write('    <priority>0.8</priority>\n')
            f.write('  </url>\n')
        f.write('</urlset>\n')
        
if __name__ == "__main__":
    generate()
