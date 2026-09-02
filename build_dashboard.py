import os
import json

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

ensure_dir("profile")

# --- Colors & Styles ---
bg_color = "#0d1117"
card_bg = "#161b22"
border_color = "#30363d"
text_primary = "#c9d1d9"
text_secondary = "#8b949e"
accent_purple = "#a371f7"
accent_green = "#3fb950"
accent_blue = "#58a6ff"
accent_yellow = "#d29922"

font_family = "system-ui, -apple-system, sans-serif"

def rounded_rect(w, h, rx=12, fill=card_bg, stroke=border_color, sw=1):
    return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" />'

def text(x, y, txt, size=14, color=text_primary, weight="normal", anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="{font_family}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{txt}</text>'

def icon_svg(x, y, path, color, size=24):
    return f'<g transform="translate({x},{y}) scale({size/24})"><path fill="{color}" d="{path}"/></g>'

# Hero SVG
hero = f'''<svg width="810" height="180" viewBox="0 0 810 180" xmlns="http://www.w3.org/2000/svg">
    {text(0, 30, ">_ Hello there! I\\'m", 16, accent_green, "500")}
    {text(0, 75, "Akbarali Nagalpara", 42, text_primary, "800")}
    {text(0, 110, "Software Engineer · Designer · Problem Solver", 18, accent_purple, "600")}
    {text(0, 145, "I design thoughtful experiences and build scalable systems", 16, text_secondary)}
    {text(0, 168, "that solve real-world problems.", 16, text_secondary)}
    
    <!-- Profile placeholder or glow -->
    <circle cx="700" cy="90" r="60" fill="{card_bg}" stroke="{border_color}" stroke-width="2"/>
    {text(700, 95, "AN", 32, text_secondary, "bold", "middle")}
    
    <!-- Availability -->
    <circle cx="630" cy="170" r="5" fill="{accent_green}"/>
    {text(645, 175, "Available for opportunities", 14, text_secondary)}
</svg>'''
with open("profile/hero.svg", "w") as f: f.write(hero)

# Buttons
btn_work = f'''<svg width="160" height="40" viewBox="0 0 160 40" xmlns="http://www.w3.org/2000/svg">
    {rounded_rect(160, 40, 8, accent_purple, accent_purple, 0)}
    {text(80, 25, "View My Work →", 14, "#ffffff", "600", "middle")}
</svg>'''
with open("profile/btn_work.svg", "w") as f: f.write(btn_work)

btn_resume = f'''<svg width="180" height="40" viewBox="0 0 180 40" xmlns="http://www.w3.org/2000/svg">
    {rounded_rect(180, 40, 8, "transparent", border_color, 1)}
    {text(90, 25, "↓ Download Resume", 14, text_primary, "600", "middle")}
</svg>'''
with open("profile/btn_resume.svg", "w") as f: f.write(btn_resume)

# Currently SVG
currently = f'''<svg width="400" height="320" viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
    {rounded_rect(400, 320)}
    {text(30, 40, "CURRENTLY", 14, text_secondary, "bold", "start",)}
    
    <g transform="translate(30, 70)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🏗️", 16, "white", "normal", "middle")}
        {text(45, 14, "Building Endpoint-IQ", 15, text_primary, "600")}
        {text(45, 32, "AI-powered API testing platform", 13, text_secondary)}
    </g>

    <g transform="translate(30, 130)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🧭", 16, "white", "normal", "middle")}
        {text(45, 14, "Exploring System Design", 15, text_primary, "600")}
        {text(45, 32, "Deepening understanding of distributed systems", 13, text_secondary)}
    </g>

    <g transform="translate(30, 190)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🧠", 16, "white", "normal", "middle")}
        {text(45, 14, "Learning", 15, text_primary, "600")}
        {text(45, 32, "Advanced Python, Cloud Architecture", 13, text_secondary)}
    </g>

    <g transform="translate(30, 250)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🎯", 16, "white", "normal", "middle")}
        {text(45, 14, "Goal", 15, text_primary, "600")}
        {text(45, 32, "Building impactful products & helping developers", 13, text_secondary)}
    </g>
</svg>'''
with open("profile/currently.svg", "w") as f: f.write(currently)

# Focus SVG
focus = f'''<svg width="400" height="320" viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg">
    {rounded_rect(400, 320)}
    {text(30, 40, "FOCUS", 14, text_secondary, "bold", "start",)}
    
    <g transform="translate(30, 70)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "⚙️", 16, "white", "normal", "middle")}
        {text(45, 14, "Backend Engineering", 15, text_primary, "600")}
        {text(45, 32, "APIs, Databases, Microservices", 13, text_secondary)}
    </g>

    <g transform="translate(30, 130)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🏛️", 16, "white", "normal", "middle")}
        {text(45, 14, "System Design", 15, text_primary, "600")}
        {text(45, 32, "Scalability, Performance, Reliability", 13, text_secondary)}
    </g>

    <g transform="translate(30, 190)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🛠️", 16, "white", "normal", "middle")}
        {text(45, 14, "Developer Experience", 15, text_primary, "600")}
        {text(45, 32, "Tools, Automation, Better DX", 13, text_secondary)}
    </g>

    <g transform="translate(30, 250)">
        <rect x="0" y="0" width="32" height="32" rx="6" fill="#1f242c" />
        {text(16, 21, "🤖", 16, "white", "normal", "middle")}
        {text(45, 14, "AI & Automation", 15, text_primary, "600")}
        {text(45, 32, "Building smart & useful products", 13, text_secondary)}
    </g>
</svg>'''
with open("profile/focus.svg", "w") as f: f.write(focus)

# Tech Stack SVG
tech = f'''<svg width="810" height="220" viewBox="0 0 810 220" xmlns="http://www.w3.org/2000/svg">
    {rounded_rect(810, 220)}
    {text(30, 40, "TECH STACK", 14, text_secondary, "bold", "start",)}
    
    <!-- Languages -->
    {text(30, 80, "Languages", 13, accent_green, "bold")}
    {text(30, 110, "Java", 15, text_primary)}
    {text(30, 135, "TypeScript", 15, text_primary)}
    {text(30, 160, "JavaScript", 15, text_primary)}
    {text(30, 185, "SQL", 15, text_primary)}

    <!-- Frontend -->
    {text(180, 80, "Frontend", 13, accent_purple, "bold")}
    {text(180, 110, "React", 15, text_primary)}
    {text(180, 135, "HTML5", 15, text_primary)}
    {text(180, 160, "CSS", 15, text_primary)}

    <!-- Backend -->
    {text(330, 80, "Backend", 13, accent_blue, "bold")}
    {text(330, 110, "Spring Boot", 15, text_primary)}
    {text(330, 135, "Hibernate", 15, text_primary)}
    {text(330, 160, "Node.js", 15, text_primary)}

    <!-- Database -->
    {text(480, 80, "Database & Infra", 13, accent_yellow, "bold")}
    {text(480, 110, "MySQL", 15, text_primary)}
    {text(480, 135, "Supabase", 15, text_primary)}
    {text(480, 160, "Docker", 15, text_primary)}

    <!-- Tools -->
    {text(630, 80, "Tools", 13, text_secondary, "bold")}
    {text(630, 110, "Git", 15, text_primary)}
    {text(630, 135, "GitHub", 15, text_primary)}
    {text(630, 160, "Apache", 15, text_primary)}
</svg>'''
with open("profile/tech_stack.svg", "w") as f: f.write(tech)

# Project Cards
def make_project(name, desc, tags, stars, forks, filename):
    tags_svg = ""
    tx = 30
    for tag in tags:
        tw = len(tag) * 8 + 16
        tags_svg += f'<rect x="{tx}" y="115" width="{tw}" height="24" rx="4" fill="#1f242c" />'
        tags_svg += text(tx + tw/2, 131, tag, 12, text_primary, "normal", "middle")
        tx += tw + 8

    proj = f'''<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
        {rounded_rect(400, 200)}
        {text(30, 45, name, 18, text_primary, "bold")}
        {text(30, 75, desc, 14, text_secondary)}
        {tags_svg}
        {text(30, 175, f"★ {stars}", 14, accent_yellow)}
        {text(80, 175, f"⑂ {forks}", 14, text_secondary)}
        {text(370, 175, "View Project →", 14, accent_blue, "600", "end")}
    </svg>'''
    with open(f"profile/{filename}", "w") as f: f.write(proj)

make_project("Endpoint-IQ", "AI-driven API testing platform with auth & parallel tests.", ["TypeScript", "API Testing", "AI"], "120", "32", "project_1.svg")
make_project("Ecommerce-Store", "Scalable e-commerce backend platform.", ["Java", "Spring Boot", "Backend"], "85", "24", "project_2.svg")

# Footer Links
def make_footer_link(name, username, filename):
    lnk = f'''<svg width="150" height="60" viewBox="0 0 150 60" xmlns="http://www.w3.org/2000/svg">
        {text(20, 25, name, 14, text_primary, "600")}
        {text(20, 45, username, 12, text_secondary)}
    </svg>'''
    with open(f"profile/{filename}", "w") as f: f.write(lnk)

make_footer_link("LinkedIn", "/in/akbaralinagalpara", "link_linkedin.svg")
make_footer_link("Portfolio", "akbarali.dev", "link_portfolio.svg")
make_footer_link("Email", "hello@akbarali.dev", "link_email.svg")
make_footer_link("GitHub", "@Akbarali-Nagalpara", "link_github.svg")
make_footer_link("Resume", "Download PDF", "link_resume.svg")

print("Generated all SVGs.")
