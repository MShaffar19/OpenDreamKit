# OpenMP
# chips: Haswell, Skylake, Bulldozer

import json
with open('glossary.json') as f:
    l = json.load(f)

output = open('glossary.tex', 'w')
output.write("\\documentclass[landscape]{article}\n\n")
output.write("\\usepackage{array}\n")
output.write("\\usepackage{url}\n")
output.write("\\usepackage{graphicx}\n")
output.write("\\usepackage[hmargin=0.6cm,vmargin=1.3cm]{geometry}\n")
output.write("\\usepackage{lmodern}\n")
# output.write("\\usepackage{avant}\n")
output.write("\\setlength{\\extrarowheight}{.5pt}\n")
output.write("\\newcommand{\\CC}{C\\nolinebreak\\hspace{-.05em}\\raisebox{.4ex}{\\tiny\\bf +}\\nolinebreak\\hspace{-.10em}\\raisebox{.4ex}{\\tiny\\bf +}}")

output.write("\\begin{document}\n")
output.write("\\thispagestyle{empty}\n")

l1 = l[:len(l)//2]
l2 = l[len(l)//2:]

for l in (l1,l2):
    output.write("\\begin{minipage}{.5\\textwidth}\n")
    if l is l1:
        output.write("\\begin{minipage}{.4\\textwidth}{\\centering \\Huge OpenDreamKit \\ Glossary}\\end{minipage}\n")
        output.write("\\hspace{.1\\textwidth}")
        output.write("\\begin{minipage}{.1\\textwidth}\\includegraphics[scale=0.15]{logos/odk.png}\\end{minipage}\n")
        output.write("\\hspace{.1\\textwidth}")
        output.write("\\begin{minipage}{.1\\textwidth}\\includegraphics[scale=0.1]{logos/europe.png}\\end{minipage}\n")
        output.write("\\vspace{.7cm}\n\n")

    output.write("\\noindent \\begin{tabular}{m{.2\\textwidth}p{.7\\textwidth}}\n")
    output.write("\\hline\n")
    for dat in l:
        if 'logo' in dat:
            scale = '[scale={}]'.format(dat['logo-rescale']) if 'logo-rescale' in dat else ''

            if dat.get('force-name'):
                output.write('\\begin{minipage}{.2\\textwidth}\n')
                output.write('{{\\large \\textbf{{{}}}}}\n\\\\'.format(dat['name']))
                output.write("\includegraphics{}{{logos/{}}}\n".format(scale, dat['logo']))
                output.write('\\end{minipage}&\n')
            else:
                output.write("\includegraphics{}{{logos/{}}} & \n".format(scale, dat['logo']))

        else:
            name = dat['acronym'] if 'acronym' in dat else dat['name']
            output.write("{{\large \\textbf{{{}}}}} & \n".format(name))

        desc = dat.get('description', '')
        if 'acronym' in dat:
            if desc:
                desc = dat['name'] + ": " + desc
            else:
                desc = dat['name']
        output.write('\\begin{tabular}{p{.7\\textwidth}}\n')
        output.write('{}\n'.format(desc))
        if 'url' in dat:
            output.write('\\\\ \\url{{{}}}'.format(dat['url']))
        output.write('\\end{tabular}\n')

        output.write('\\\\\hline\n')
    output.write("\\end{tabular}\n")
    output.write("\\end{minipage}\n")

output.write("\\end{document}\n")


