import os

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

cards_html = """
                <!-- Project 4: MULTI-AGENT DASHBOARD -->
                <div id="project-multiagent" class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MULTI-AGENT // AI PIPELINE ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider">SIH HACKATHON</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">MULTI-AGENT DASHBOARD</h3>
                    </div>
                    
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        A multi-agent AI productivity dashboard developed for the SIH. It features LangGraph orchestration, Google Gemini as the reasoning engine, and a Neubrutalist UI design.
                    </p>

                    <div class="mt-auto">
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">LANGGRAPH</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">GEMINI 2.5</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">UI DESIGN</span>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <a href="https://github.com/tejuas98/ulti-agent-productivity-workforce" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">PROTOTYPE // GITHUB</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--card-text)] group-hover:text-[var(--text-primary)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 5: MEDICARE -->
                <div id="project-medicare" class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ HEALTHCARE // WEB APP ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider opacity-0 select-none">SPACER</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">MEDICARE</h3>
                    </div>
                    
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        A Medicare web application featuring robust system architecture diagrams. Built with modern web tooling for rapid performance and clean healthcare data visualization.
                    </p>

                    <div class="mt-auto">
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">VITE</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">TAILWINDCSS</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">JAVASCRIPT</span>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <a href="https://github.com/tejuas98/medicare" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
                                <span class="font-mono font-black text-xs uppercase text-[var(--card-text)] group-hover:text-[var(--text-primary)]">PROTOTYPE // GITHUB</span>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" class="text-[var(--card-text)] group-hover:text-[var(--text-primary)]" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Project 6: RAAHAT -->
                <div id="project-raahat" class="selected-work-card">
                    <div class="mb-4">
                        <span class="font-mono text-[9px] font-bold tracking-[0.2em] text-[var(--arsenal-text)] block mb-2 uppercase">[ MOBILE NATIVE // APP ]</span>
                        <div class="flex flex-wrap gap-2 mb-3">
                            <span class="bg-[var(--bg-secondary)] text-[var(--text-primary)] font-mono text-[9px] px-2 py-1 uppercase tracking-wider opacity-0 select-none">SPACER</span>
                        </div>
                        <h3 class="font-serif font-black text-3xl tracking-tighter leading-[1] uppercase text-[var(--card-text)]">RAAHAT</h3>
                    </div>
                    
                    <p class="font-sans font-medium text-sm leading-relaxed text-[var(--card-text)] mb-6 flex-grow">
                        Cross-platform mobile application utilizing Expo for rapid native deployment and feature testing.
                    </p>

                    <div class="mt-auto">
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">REACT NATIVE</span>
                            <span class="border-[2px] border-[var(--card-border)] text-[var(--card-text)] font-sans font-bold text-[10px] px-2 py-1 uppercase">EXPO</span>
                        </div>
                        
                        <div class="flex flex-col gap-2">
                            <a href="https://github.com/tejuas98/Raahat" target="_blank" rel="noopener noreferrer" class="bg-transparent border-[3px] border-[var(--card-border)] px-4 py-2 flex justify-between items-center group hover:bg-[var(--bg-secondary)] transition-colors">
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
