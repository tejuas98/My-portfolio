import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '    <!-- SECTION: THE NETWORK -->'
end_marker = '    <!-- SECTION: DEPLOYMENTS (FIELD WORK) -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find start or end markers.")
    exit(1)

new_network_section = """    <!-- SECTION: THE NETWORK -->
    <section id="network" class="section-page relative overflow-hidden bg-[var(--bg-primary)] border-t-[3px] border-[var(--border-dark)]">
        <div class="px-6 md:px-12 lg:px-24 max-w-[1600px] mx-auto py-24">
            
            <div class="mb-16 stagger-element">
                <h2 class="font-mono font-black text-lg mb-4 tracking-[0.2em] uppercase opacity-40 text-[var(--text-primary)]">THE NETWORK // LIVE SYSTEMS</h2>
                <div class="w-16 h-[3px] bg-[var(--text-primary)] mb-6"></div>
                <p class="font-sans font-bold text-[var(--text-primary)] max-w-3xl leading-relaxed text-base md:text-lg opacity-80">
                    These are not isolated pages. This is my public network of research, career intelligence, design archives, and learning systems.
                </p>
            </div>

            <!-- PRIMARY NODES (Row 1: 3 Columns) -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 stagger-element mb-12">
                
                <!-- MY RESEARCH -->
                <div class="border-[3px] border-[var(--text-primary)] bg-[var(--bg-primary)] p-8 flex flex-col group relative shadow-[8px_8px_0_0_var(--text-primary)] hover:translate-y-[2px] hover:translate-x-[2px] hover:shadow-[6px_6px_0_0_var(--text-primary)] transition-all">
                    <div class="mb-6">
                        <div class="flex items-center justify-between mb-4">
                            <span class="font-mono text-[10px] font-bold tracking-[0.2em] text-[var(--text-secondary)] uppercase group-hover:text-[var(--arsenal-text)] transition-colors">[ RESEARCH NODE ]</span>
                            <span class="border-[2px] border-[var(--text-primary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider font-bold">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl xl:text-4xl tracking-tighter leading-[1] uppercase text-[var(--text-primary)]">MY RESEARCH</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--text-secondary)] mb-8 flex-grow">
                        Research papers, micro-tool workflows, guides, experiments, and original writing.
                    </p>
                    <div class="mt-auto flex flex-col gap-3">
                        <a href="https://tejuas98.github.io/My-research/" target="_blank" class="bg-[var(--text-primary)] border-[3px] border-[var(--text-primary)] text-[var(--bg-primary)] px-4 py-3 flex justify-between items-center hover:bg-transparent hover:text-[var(--text-primary)] transition-all">
                            <span class="font-mono font-black text-xs uppercase">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/My-research" target="_blank" class="bg-transparent border-[3px] border-[var(--text-primary)] px-4 py-3 flex justify-between items-center text-[var(--text-primary)] hover:bg-[var(--text-primary)] hover:text-[var(--bg-primary)] transition-all">
                            <span class="font-mono font-black text-xs uppercase">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- JOBS & CAREER ROLES -->
                <div class="border-[3px] border-[var(--text-primary)] bg-[var(--bg-primary)] p-8 flex flex-col group relative shadow-[8px_8px_0_0_var(--text-primary)] hover:translate-y-[2px] hover:translate-x-[2px] hover:shadow-[6px_6px_0_0_var(--text-primary)] transition-all">
                    <div class="mb-6">
                        <div class="flex items-center justify-between mb-4">
                            <span class="font-mono text-[10px] font-bold tracking-[0.2em] text-[var(--text-secondary)] uppercase group-hover:text-[var(--arsenal-text)] transition-colors">[ CAREER INTELLIGENCE ]</span>
                            <span class="border-[2px] border-[var(--text-primary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider font-bold">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl xl:text-4xl tracking-tighter leading-[1] uppercase text-[var(--text-primary)]">JOBS & CAREER ROLES</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--text-secondary)] mb-8 flex-grow">
                        Career research guide for future-relevant AI, ML, safety, infrastructure, research, and engineering roles.
                    </p>
                    <div class="mt-auto flex flex-col gap-3">
                        <a href="https://tejuas98.github.io/Jobs/" target="_blank" class="bg-[var(--text-primary)] border-[3px] border-[var(--text-primary)] text-[var(--bg-primary)] px-4 py-3 flex justify-between items-center hover:bg-transparent hover:text-[var(--text-primary)] transition-all">
                            <span class="font-mono font-black text-xs uppercase">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/Jobs" target="_blank" class="bg-transparent border-[3px] border-[var(--text-primary)] px-4 py-3 flex justify-between items-center text-[var(--text-primary)] hover:bg-[var(--text-primary)] hover:text-[var(--bg-primary)] transition-all">
                            <span class="font-mono font-black text-xs uppercase">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- VISUAL RESEARCH LAB -->
                <div class="border-[3px] border-[var(--text-primary)] bg-[var(--bg-primary)] p-8 flex flex-col group relative shadow-[8px_8px_0_0_var(--text-primary)] hover:translate-y-[2px] hover:translate-x-[2px] hover:shadow-[6px_6px_0_0_var(--text-primary)] transition-all">
                    <div class="mb-6">
                        <div class="flex items-center justify-between mb-4">
                            <span class="font-mono text-[10px] font-bold tracking-[0.2em] text-[var(--text-secondary)] uppercase group-hover:text-[var(--arsenal-text)] transition-colors">[ DESIGN ARCHIVE ]</span>
                            <span class="border-[2px] border-[var(--text-primary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider font-bold">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl xl:text-4xl tracking-tighter leading-[1] uppercase text-[var(--text-primary)]">VISUAL RESEARCH LAB</h3>
                    </div>
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--text-secondary)] mb-8 flex-grow">
                        A curated archive of designs, diagrams, interfaces, and visual inspiration.
                    </p>
                    <div class="mt-auto flex flex-col gap-3">
                        <a href="https://tejuas98.github.io/my-collections-of-design-/" target="_blank" class="bg-[var(--text-primary)] border-[3px] border-[var(--text-primary)] text-[var(--bg-primary)] px-4 py-3 flex justify-between items-center hover:bg-transparent hover:text-[var(--text-primary)] transition-all">
                            <span class="font-mono font-black text-xs uppercase">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/my-collections-of-design-" target="_blank" class="bg-transparent border-[3px] border-[var(--text-primary)] px-4 py-3 flex justify-between items-center text-[var(--text-primary)] hover:bg-[var(--text-primary)] hover:text-[var(--bg-primary)] transition-all">
                            <span class="font-mono font-black text-xs uppercase">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

            </div>

            <!-- PRESENTATION NODES (Row 2: Ledger Rows) -->
            <div class="flex flex-col gap-4 stagger-element">
                
                <!-- CYBERSECURITY -->
                <div class="border-[3px] border-[var(--text-primary)] bg-[var(--bg-primary)] p-6 flex flex-col md:flex-row md:items-center justify-between relative shadow-[4px_4px_0_0_var(--text-primary)] hover:translate-y-[2px] hover:translate-x-[2px] hover:shadow-[2px_2px_0_0_var(--text-primary)] transition-all group">
                    <div class="flex-grow mb-6 md:mb-0 md:pr-8">
                        <div class="flex items-center gap-4 mb-3">
                            <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--text-secondary)] uppercase group-hover:text-[var(--arsenal-text)] transition-colors">[ PRESENTATION NODE ]</span>
                            <span class="border-[2px] border-[var(--text-primary)] text-[var(--text-primary)] font-mono text-[8px] px-1.5 py-0.5 uppercase tracking-wider font-bold">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--text-primary)] mb-2">CYBERSECURITY</h3>
                        <p class="font-sans font-medium text-sm text-[var(--text-secondary)]">
                            Cybersecurity presentation and learning website.
                        </p>
                    </div>
                    <div class="flex flex-col sm:flex-row md:flex-col lg:flex-row gap-3 min-w-[280px] lg:min-w-[320px]">
                        <a href="https://tejuas98.github.io/CyberSecurity/" target="_blank" class="flex-1 bg-[var(--text-primary)] border-[3px] border-[var(--text-primary)] text-[var(--bg-primary)] px-4 py-2.5 flex justify-between items-center hover:bg-transparent hover:text-[var(--text-primary)] transition-all">
                            <span class="font-mono font-black text-[11px] uppercase">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/CyberSecurity" target="_blank" class="flex-1 bg-transparent border-[3px] border-[var(--text-primary)] text-[var(--text-primary)] px-4 py-2.5 flex justify-between items-center hover:bg-[var(--text-primary)] hover:text-[var(--bg-primary)] transition-all">
                            <span class="font-mono font-black text-[11px] uppercase">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

                <!-- MAYA EXANA -->
                <div class="border-[3px] border-[var(--text-primary)] bg-[var(--bg-primary)] p-6 flex flex-col md:flex-row md:items-center justify-between relative shadow-[4px_4px_0_0_var(--text-primary)] hover:translate-y-[2px] hover:translate-x-[2px] hover:shadow-[2px_2px_0_0_var(--text-primary)] transition-all group">
                    <div class="flex-grow mb-6 md:mb-0 md:pr-8">
                        <div class="flex items-center gap-4 mb-3">
                            <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--text-secondary)] uppercase group-hover:text-[var(--arsenal-text)] transition-colors">[ PRESENTATION NODE ]</span>
                            <span class="border-[2px] border-[var(--text-primary)] text-[var(--text-primary)] font-mono text-[8px] px-1.5 py-0.5 uppercase tracking-wider font-bold">LIVE</span>
                        </div>
                        <h3 class="font-serif font-black text-2xl tracking-tighter leading-[1] uppercase text-[var(--text-primary)] mb-2">MAYA EXANA</h3>
                        <p class="font-sans font-medium text-sm text-[var(--text-secondary)]">
                            Project with presentation and live hosted site.
                        </p>
                    </div>
                    <div class="flex flex-col sm:flex-row md:flex-col lg:flex-row gap-3 min-w-[280px] lg:min-w-[320px]">
                        <a href="https://tejuas98.github.io/maya-exana/" target="_blank" class="flex-1 bg-[var(--text-primary)] border-[3px] border-[var(--text-primary)] text-[var(--bg-primary)] px-4 py-2.5 flex justify-between items-center hover:bg-transparent hover:text-[var(--text-primary)] transition-all">
                            <span class="font-mono font-black text-[11px] uppercase">LIVE ↗</span>
                        </a>
                        <a href="https://github.com/tejuas98/maya-exana" target="_blank" class="flex-1 bg-transparent border-[3px] border-[var(--text-primary)] text-[var(--text-primary)] px-4 py-2.5 flex justify-between items-center hover:bg-[var(--text-primary)] hover:text-[var(--bg-primary)] transition-all">
                            <span class="font-mono font-black text-[11px] uppercase">GITHUB ↗</span>
                        </a>
                    </div>
                </div>

            </div>

        </div>
    </section>
    
"""

new_content = content[:start_idx] + new_network_section + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated THE NETWORK successfully.")
