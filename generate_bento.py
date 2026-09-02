import os

# --- Colors & Styles ---
bg_color = "#0d1117"
border_color = "#1f2328" # Subtle
text_primary = "#c9d1d9"
text_secondary = "#8b949e"
accent_color = "#00d2ff"
font_family = "system-ui, -apple-system, sans-serif"

def rounded_rect(x, y, w, h, rx):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5" />'

def label_text(x, y, text):
    return f'<text x="{x}" y="{y}" font-family="{font_family}" font-size="12" font-weight="600" fill="{text_secondary}" letter-spacing="1.5">{text}</text>'

def title_text(x, y, text):
    return f'<text x="{x}" y="{y}" font-family="{font_family}" font-size="28" font-weight="bold" fill="{text_primary}">{text}</text>'

def body_text(x, y, text, size=16, color=text_primary):
    return f'<text x="{x}" y="{y}" font-family="{font_family}" font-size="{size}" fill="{color}">{text}</text>'

svg_elements = []

# Header
svg_elements.append(f'<svg width="1200" height="800" viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">')
svg_elements.append(f'<defs><style>text {{ font-family: {font_family}; }}</style></defs>')

# --- Row 1 ---
# Location (x=0, y=0, w=400, h=200)
cx, cy, cw, ch = 0, 0, 400, 200
svg_elements.append(rounded_rect(cx, cy, cw, ch, 20))
svg_elements.append(label_text(cx + 40, cy + 50, "LOCATION"))
svg_elements.append(title_text(cx + 40, cy + 120, "📍 India"))

# Featured Work (x=430, y=0, w=770, h=200)
cx, cy, cw, ch = 430, 0, 770, 200
svg_elements.append(rounded_rect(cx, cy, cw, ch, 20))
svg_elements.append(label_text(cx + 40, cy + 50, "FEATURED WORK"))
svg_elements.append(title_text(cx + 40, cy + 110, "Building scalable backend systems"))
svg_elements.append(body_text(cx + 40, cy + 150, "Focused on high-performance architecture and resilient APIs.", 16, text_secondary))

# --- Row 2 ---
# Engineering Focus (x=0, y=230, w=770, h=260)
cx, cy, cw, ch = 0, 230, 770, 260
svg_elements.append(rounded_rect(cx, cy, cw, ch, 20))
svg_elements.append(label_text(cx + 40, cy + 50, "ENGINEERING FOCUS"))
svg_elements.append(body_text(cx + 40, cy + 100, "⚡ Backend Architecture", 18))
svg_elements.append(body_text(cx + 40, cy + 135, "🏗️ System Design", 18))
svg_elements.append(body_text(cx + 40, cy + 170, "🔌 APIs", 18))
svg_elements.append(body_text(cx + 40, cy + 205, "🗄️ Databases", 18))
svg_elements.append(body_text(cx + 40, cy + 240, "🚀 Scalable Applications", 18))

# Currently Building (x=800, y=230, w=400, h=260)
cx, cy, cw, ch = 800, 230, 400, 260
svg_elements.append(rounded_rect(cx, cy, cw, ch, 20))
svg_elements.append(label_text(cx + 40, cy + 50, "CURRENTLY BUILDING"))
svg_elements.append(body_text(cx + 40, cy + 110, "⚙️ Backend systems", 18))
svg_elements.append(body_text(cx + 40, cy + 160, "🛠️ Developer tools", 18))
svg_elements.append(body_text(cx + 40, cy + 210, "🌐 Scalable applications", 18))

# --- Row 3 ---
# GitHub Activity (x=0, y=520, w=400, h=280)
cx, cy, cw, ch = 0, 520, 400, 280
svg_elements.append(rounded_rect(cx, cy, cw, ch, 20))
svg_elements.append(label_text(cx + 40, cy + 50, "GITHUB ACTIVITY"))
# A visual representation of a contribution graph (simplified)
gx, gy = cx + 40, cy + 100
for row in range(5):
    for col in range(12):
        color = "#161b22"
        if (col + row) % 3 == 0: color = "#006688"
        if (col * row) % 5 == 0: color = "#00d2ff"
        svg_elements.append(f'<rect x="{gx + col*26}" y="{gy + row*26}" width="20" height="20" rx="4" fill="{color}" opacity="0.8" />')

svg_elements.append(body_text(cx + 40, cy + 250, "Continuous learning & building", 14, text_secondary))

# Tech Stack (x=430, y=520, w=770, h=280)
cx, cy, cw, ch = 430, 520, 770, 280
svg_elements.append(rounded_rect(cx, cy, cw, ch, 20))
svg_elements.append(label_text(cx + 40, cy + 50, "TECH STACK"))

# Backend
svg_elements.append(body_text(cx + 40, cy + 100, "BACKEND", 12, accent_color))
svg_elements.append(body_text(cx + 40, cy + 125, "Java · Spring Boot · Hibernate", 16))

# Frontend
svg_elements.append(body_text(cx + 40, cy + 175, "FRONTEND", 12, accent_color))
svg_elements.append(body_text(cx + 40, cy + 200, "React · JavaScript · HTML5", 16))

# Database
svg_elements.append(body_text(cx + 450, cy + 100, "DATABASE", 12, accent_color))
svg_elements.append(body_text(cx + 450, cy + 125, "MySQL · Supabase", 16))

# Other
svg_elements.append(body_text(cx + 450, cy + 175, "OTHER", 12, accent_color))
svg_elements.append(body_text(cx + 450, cy + 200, "Apache · C", 16))


svg_elements.append("</svg>")

with open("profile/bento-grid.svg", "w") as f:
    f.write("\n".join(svg_elements))

print("Created profile/bento-grid.svg")
