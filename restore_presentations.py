import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

presentations_html = """
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
"""

deployments_idx = content.find('<!-- SECTION: DEPLOYMENTS (FIELD WORK) -->')
insert_idx = content.rfind('            </div>\n        </div>\n    </section>', 0, deployments_idx)

if insert_idx != -1:
    new_content = content[:insert_idx] + presentations_html + content[insert_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Restored presentations successfully.")
else:
    print("Insertion point not found.")
