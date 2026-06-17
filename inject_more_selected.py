import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

cards_html = """
                <!-- Project 7: ELIVAMUSTO -->
                <div id="project-elivamusto" class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ WEB EXPERIENCE // FULL STACK ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider opacity-0 select-none">SPACER</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">ELIVAMUSTO</h3>
                    </div>
                    
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Hosted web project featuring dynamic interface design and robust frontend architecture.
                    </p>

                    <div class="mt-auto">
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">WEB DEV</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">UI DESIGN</span>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <a href="https://tejuas98.github.io/elivamusto/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                            </a>
                            <a href="https://github.com/tejuas98/elivamusto" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">PROTOTYPE // GITHUB</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--card-text)] group-hover:text-[var(--text-primary)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 8: MACROPAD -->
                <div id="project-macropad" class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ HARDWARE // ELECTRONICS ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider opacity-0 select-none">SPACER</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">MY FIRST MACROPAD</h3>
                    </div>
                    
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Custom macropad hardware project, integrating physical electronics with firmware design for optimized productivity workflows.
                    </p>

                    <div class="mt-auto">
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">HARDWARE</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">FIRMWARE</span>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <a href="https://github.com/tejuas98/my-first-macropad" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">PROTOTYPE // GITHUB</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--card-text)] group-hover:text-[var(--text-primary)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 9: SUIP -->
                <div id="project-suip" class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ WEB EXPERIENCE // INTERACTIVE ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider opacity-0 select-none">SPACER</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">SUIP</h3>
                    </div>
                    
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        An interactive hosted web project demonstrating clean UI methodologies and responsive design patterns.
                    </p>

                    <div class="mt-auto">
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">WEB DEV</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">UI DESIGN</span>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <a href="https://tejuas98.github.io/suip/" target="_blank" rel="noopener noreferrer" class="bg-[var(--bg-primary)] border-[3px] border-[var(--border-dark)] px-4 py-2 flex justify-between items-center group hover:bg-transparent transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]">LIVE ↗</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--text-primary)] group-hover:text-[var(--arsenal-text)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                            </a>
                            <a href="https://github.com/tejuas98/suip" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">PROTOTYPE // GITHUB</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--card-text)] group-hover:text-[var(--text-primary)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                            </a>
                        </div>
                    </div>
                </div>
"""

target = """                            </a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

replacement = """                            </a>
                        </div>
                    </div>
                </div>
""" + cards_html + """
            </div>
        </div>
    </section>"""

if target in content:
    content = content.replace(target, replacement)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected successfully.")
else:
    print("Target not found.")
