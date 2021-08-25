from jinja2 import Template

tmp_txt = '{"a":"{{aaa}}","b":"{{aaa}}","c":"{{aaa}}","d":"{{aaa}}","e":"{{aaa}}"' \
          ',"f":"{{aaa}}","g":"{{aaa}}","h":"{{aaa}}","i":"{{aaa}}","j":"{{aaa}}"' \
          ',"k":"{{aaa}}","l":"{{aaa}}","m":"{{aaa}}","n":"{{aaa}}","o":"{{aaa}}"' \
          ',"p":"{{aaa}}","q":"{{aaa}}","r":"{{aaa}}","s":"{{aaa}}","t":"{{aaa}}"' \
          ',"u":"{{aaa}}","v":"{{aaa}}","w":"{{aaa}}","x":"{{aaa}}","y":"{{aaa}}"' \
          ',"z":"{{aaa}}","a1":"{{aaa}}","b2":"{{aaa}}","c3":"{{aaa}}","cd4":"{{aaa}}"}'
template = Template(tmp_txt)

disp_text = ""
for i in range(30):
    data = {'aaa': str(i)*30}
    disp_text = f'{disp_text}{template.render(data)}\n'
with open("sample.txt", "w") as f:
    f.write(disp_text)
