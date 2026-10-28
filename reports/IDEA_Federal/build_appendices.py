import os
R='/workspace/idea-corpus/'
WITHHOLD={'artifacts/federal/federal_reviewer_log.md':{80:'describes the researcher\'s private rules files'}}
def block(path, lines=None):
    L=open(R+path,encoding='utf-8').read().split('\n')
    if L and L[-1]=='': L=L[:-1]
    idx=lines or range(1,len(L)+1)
    W=WITHHOLD.get(path,{})
    out=['```']+[(f'{path}:{i}: [withheld: {W[i]}]' if i in W else f'{path}:{i}: {L[i-1]}') for i in idx]+['```','']
    return '\n'.join(out)
A=[]
A.append('# Appendices: verbatim quotations with file:line pins\n')
A.append('Each line below is copied byte for byte from the named file, prefixed with its path and line number. Nothing inside the code blocks is my prose. Em dashes that appear inside these blocks are in the source files (9 occur in federal_reviewer_log.md: 8 at lines 2, 7, 15, 18, 22, 24, 30 and 37, which a background worker wrote on 2026-10-15, and 1 at line 210 inside a quotation of a federal regulation). Times printed as "PST" on 2026-10-15 are UTC minus 8 as written; section 2 gives the correct PDT.\n')
A.append('Not quoted, for privacy or confidentiality: my check-in file (audit/checkin/), rules_audit.md, the researcher\'s rules files, Design Memo #3, and any personal or case material. Those are described in prose where needed and are not in this repository. Withheld by pin: federal_reviewer_log.md:80 (it describes the researcher\'s private rules files) and project-root status.md:87 (left out of Appendix D for the same reason).\n')
A.append('## Appendix A. Reviewer log (artifacts/federal/federal_reviewer_log.md, all lines)\n')
A.append(block('artifacts/federal/federal_reviewer_log.md'))
A.append('## Appendix B. Status lines (artifacts/federal/status.md, all lines)\n')
A.append(block('artifacts/federal/status.md'))
A.append('## Appendix C. Source records\n')
for p in ['artifacts/federal/src/usc/CAPTURE_LOG.txt','artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt','artifacts/federal/src/CAPTURE_LOG_guidance.txt',
          'artifacts/federal/src/official/rowley_458us176_provenance.txt','artifacts/federal/src/official/honig_484us305_provenance.txt',
          'artifacts/federal/src/official/endrew_f_15-827_provenance.txt','artifacts/federal/src/official/fry_15-497_provenance.txt']:
    A.append(f'### {p}\n'); A.append(block(p))
A.append('## Appendix D. IDEA Federal lines in the project status file (status.md at the project root)\n')
A.append(block('status.md',[13,48,55,138,166]))
open('appendices.md','w').write('\n'.join(A))
body=open('report_body.md').read().rstrip('\n')
open('IDEA_Federal_Process_Report_PRISMA_2026-10-28.md','w').write(body+'\n\n'+'\n'.join(A))
