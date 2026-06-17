import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target_start = '                <!-- MAJOR PROJECTS -->'
target_end = '    <!-- SECTION: DEPLOYMENTS (FIELD WORK) -->'

start_idx = content.find(target_start)
end_idx = content.find(target_end, start_idx)

if start_idx != -1 and end_idx != -1:
    # We want to keep everything up to target_start, and everything from target_end onwards.
    # But wait, we need to preserve the closing tags for THE NETWORK section:
    #             </div>
    #         </div>
    #     </section>
    
    # Let's look for the closing tags right before target_end
    closing_tags = '            </div>\n        </div>\n    </section>\n    \n'
    
    # So we replace from start_idx to the start of closing_tags with nothing
    closing_idx = content.rfind(closing_tags, start_idx, end_idx)
    
    if closing_idx != -1:
        new_content = content[:start_idx] + content[closing_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Deleted successfully")
    else:
        print("Could not find closing tags")
else:
    print("Could not find start or end index.")
