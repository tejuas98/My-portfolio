import os

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation
nav_search = '<a href="#selected-work" class="nav-link">SELECTED WORK</a>'
nav_replace = '<a href="#selected-work" class="nav-link">SELECTED WORK</a>\n            <a href="#network" class="nav-link">THE NETWORK</a>'
if nav_search in content and '<a href="#network" class="nav-link">THE NETWORK</a>' not in content:
    content = content.replace(nav_search, nav_replace)

# 2. Update Footer
footer_search = '<a href="https://tejuas98.github.io/my-collections-of-design-/" class="hover:text-[var(--arsenal-text)] transition-colors">Design Lab</a>'
footer_replace = '<a href="https://tejuas98.github.io/my-collections-of-design-/" class="hover:text-[var(--arsenal-text)] transition-colors">Design Lab</a> &middot; \n                <a href="https://github.com/tejuas98" class="hover:text-[var(--arsenal-text)] transition-colors">GitHub</a> &middot; \n                <a href="https://www.linkedin.com/in/tejus98" class="hover:text-[var(--arsenal-text)] transition-colors">LinkedIn</a>'
if footer_search in content and 'GitHub</a> &middot;' not in content:
    content = content.replace(footer_search, footer_replace)

# 3. Add The Network Section
network_section = """
    <!-- SECTION: THE NETWORK -->
    <section id="network" class="section-page relative overflow-hidden">
        <div class="px-6 md:px-12 lg:px-24 max-w-[1600px] mx-auto py-20">
            <div class="mb-12 stagger-element">
                <h2 class="font-mono font-black text-lg mb-4 tracking-[0.2em] uppercase opacity-40 text-[var(--text-primary)]">THE NETWORK // LIVE SYSTEMS</h2>
                <div class="w-12 h-1 bg-[var(--text-primary)]"></div>
                <p class="font-sans text-[var(--text-secondary)] text-base max-w-3xl leading-relaxed mt-6">
                    These are not isolated projects. This is my public network of builds: research, career intelligence, design archives, AI tools, presentations, and shipped experiments.
                </p>
            </div>

            <!-- Bento Box Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 stagger-element">
                
                <!-- 1. MAIN HUB -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAIN HUB / SOCIALS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">GITHUB</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Main Portfolio</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Central portfolio hub for my projects, research, design archive, and career guides.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/My-portfolio/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/My-portfolio" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- SOCIALS -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAIN HUB / SOCIALS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">ACTIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Social Links</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Connect with me across the network.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://github.com/tejuas98" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                        <a href="https://www.linkedin.com/in/tejus98" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">LINKEDIN ↗</span>
                        </a>
                        <a href="https://www.youtube.com/@tejus_98" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">YOUTUBE ↗</span>
                        </a>
                        <a href="https://x.com/tejus_98" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">X / TWITTER ↗</span>
                        </a>
                        <a href="https://www.instagram.com/tejus.98/" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">INSTAGRAM ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 2. RESEARCH & WRITING -->
                <div class="selected-work-card lg:col-span-2">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ RESEARCH & WRITING ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">GITHUB</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">My Research</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Research papers, micro-tool workflows, guides, experiments, and original writing.
                    </p>
                    <div class="mt-auto flex flex-col md:flex-row gap-2">
                        <a href="https://tejuas98.github.io/My-research/" target="_blank" rel="noopener noreferrer" class="flex-1 bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/My-research" target="_blank" rel="noopener noreferrer" class="flex-1 bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 3. CAREER INTELLIGENCE -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ CAREER INTELLIGENCE ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Jobs & Career Roles</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Career research guide for future-relevant AI, ML, safety, infrastructure, research, and engineering roles.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/Jobs/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/Jobs" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 4. DESIGN ARCHIVE -->
                <div class="selected-work-card lg:col-span-2">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ DESIGN ARCHIVE ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">ARCHIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Visual Research Lab</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        A curated archive of designs, diagrams, interfaces, and visual inspiration.
                    </p>
                    <div class="mt-auto flex flex-col md:flex-row gap-2">
                        <a href="https://tejuas98.github.io/my-collections-of-design-/" target="_blank" rel="noopener noreferrer" class="flex-1 bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/my-collections-of-design-" target="_blank" rel="noopener noreferrer" class="flex-1 bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: Scriptify -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">SIH FINALIST</span>
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">APP</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Scriptify</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        SIH 2025 Grand Finalist project. Offline-first AI transliteration app using OCR, React Native, Node.js, Firebase, Google Vision/Tesseract.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://github.com/tejuas98/scriptify" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: IKS Weather -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">IKS Weather Report Builder</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Weather report generator that creates print-ready analytical reports from hourly weather data.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/IKS-Weather-Report-Builder/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/IKS-Weather-Report-Builder" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: Multi-Agent -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">GITHUB</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Multi-Agent Productivity</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Multi-agent AI productivity dashboard using LangGraph, Google Gemini, and Neubrutalist UI.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://github.com/tejuas98/ulti-agent-productivity-workforce" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: Raahat -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">APP</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Raahat</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        React Native / Expo app project.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://github.com/tejuas98/Raahat" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: Medicare -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">GITHUB</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Medicare</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Medicare web application built with Vite, TailwindCSS, and JavaScript.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://github.com/tejuas98/medicare" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: Elivamusto -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Elivamusto</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Hosted web project.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/elivamusto/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/elivamusto" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 5. MAJOR PROJECTS: Macropad -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MAJOR PROJECTS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">HARDWARE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">My First Macropad</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Custom macropad project.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://github.com/tejuas98/my-first-macropad" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 6. PRESENTATIONS / LEARNING: CyberSecurity -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ PRESENTATIONS / LEARNING ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">CyberSecurity</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Cybersecurity presentation/website.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/CyberSecurity/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/CyberSecurity" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 6. PRESENTATIONS / LEARNING: Maya Exana -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ PRESENTATIONS / LEARNING ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Maya Exana</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Project with presentation and live hosted site.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/maya-exana/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/maya-exana" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- 6. PRESENTATIONS / LEARNING: Suip -->
                <div class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ PRESENTATIONS / LEARNING ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">Suip</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Hosted web project.
                    </p>
                    <div class="mt-auto flex flex-col gap-2">
                        <a href="https://tejuas98.github.io/suip/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/suip" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                            <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# Inject before DEPLOYMENTS
if '<section id="network"' not in content:
    content = content.replace('    <!-- SECTION: DEPLOYMENTS (FIELD WORK) -->', network_section + '\n    <!-- SECTION: DEPLOYMENTS (FIELD WORK) -->')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification complete.")
