"""Shared brand pieces for the site: the CodeNinja logo (parent site mark, white wordmark for the
dark pages) and the beta access form. The form composes an email to hello@codeninjaconsulting.com,
CodeNinja's inbound address; nothing is stored or sent by this static site.
"""
PARENT = "https://codeninjaconsulting.com"
INBOX = "hello@codeninjaconsulting.com"
LOGO = '<svg role="img" aria-label="CodeNinja" class="logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 223 34" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M7.95375 17.2038L24.2351 22.5743L27.8041 33.0773L0 22.1664V12.0712L27.8721 0.922363L24.2351 11.6633L7.95375 17.2038ZM51.3942 17.2037L35.1128 11.6972L31.6118 0.990234L59.348 12.0711V22.1663L31.6798 33.0092L35.1128 22.5402L51.3942 17.2037Z" fill="#E31E30"></path><path d="M70.8394 22.8223V10.5735C70.8394 9.18758 71.2631 8.07586 72.1106 7.23833C72.9581 6.39083 74.0648 5.96709 75.4308 5.96709H85.3764V8.88347L84.0005 10.2594H77.2704C76.044 10.2594 75.4308 10.8726 75.4308 12.099V21.2819C75.4308 22.5082 76.044 23.1214 77.2704 23.1214H85.3764V27.4138H75.4308C74.0648 27.4138 72.9581 26.995 72.1106 26.1575C71.2631 25.3199 70.8394 24.2082 70.8394 22.8223Z" fill="#FFFFFF"></path><path d="M93.9611 23.4355H97.4757C98.7021 23.4355 99.3153 22.8223 99.3153 21.5959V11.7999C99.3153 10.5735 98.7021 9.96029 97.4757 9.96029H93.9611C92.7347 9.96029 92.1215 10.5735 92.1215 11.7999V21.5959C92.1215 22.8223 92.7347 23.4355 93.9611 23.4355ZM87.5301 23.1214V10.2594C87.5301 8.8735 87.9538 7.76179 88.8013 6.92426C89.6488 6.08673 90.7555 5.66797 92.1215 5.66797H99.3153C100.701 5.66797 101.813 6.08673 102.65 6.92426C103.488 7.76179 103.907 8.8735 103.907 10.2594V23.1214C103.907 24.5073 103.488 25.6191 102.65 26.4566C101.813 27.2941 100.701 27.7129 99.3153 27.7129H92.1215C90.7555 27.7129 89.6488 27.2941 88.8013 26.4566C87.9538 25.6191 87.5301 24.5073 87.5301 23.1214Z" fill="#FFFFFF"></path><path d="M107.571 27.4138V5.96709H119.057C120.443 5.96709 121.555 6.38585 122.392 7.22338C123.23 8.0609 123.648 9.17761 123.648 10.5735V22.8223C123.648 24.2082 123.23 25.3199 122.392 26.1575C121.555 26.995 120.443 27.4138 119.057 27.4138H107.571ZM112.162 23.1214H117.217C118.444 23.1214 119.057 22.5082 119.057 21.2819V12.099C119.057 10.8726 118.444 10.2594 117.217 10.2594H112.162V23.1214Z" fill="#FFFFFF"></path><path d="M127.313 27.4138V5.96709H141.251V8.88347L139.875 10.2594H131.904V14.5517H138.185V18.6795H131.904V23.1214H141.251V27.4138H127.313Z" fill="#FFFFFF"></path><path d="M144.302 27.4138V5.96709H149.357L156.551 19.4573H156.716L156.252 15.6286V5.96709H160.844V27.4138H155.789L148.595 13.9385H148.445L148.894 17.7672V27.4138H144.302Z" fill="#FFFFFF"></path><path d="M164.822 27.4138V5.96709H169.413V27.4138H164.822Z" fill="#FFFFFF"></path><path d="M173.406 27.4138V5.96709H178.462L185.655 19.4573H185.82L185.356 15.6286V5.96709H189.948V27.4138H184.893L177.699 13.9385H177.549L177.998 17.7672V27.4138H173.406Z" fill="#FFFFFF"></path><path d="M192.236 27.7129V23.4355H196.992C198.218 23.4355 198.831 22.8223 198.831 21.5959V5.96709H203.423V23.1214C203.423 24.5073 202.999 25.6191 202.152 26.4566C201.304 27.2941 200.197 27.7129 198.831 27.7129H192.236Z" fill="#FFFFFF"></path><path d="M211.514 19.1432H216.405L214.116 10.1099H213.802L211.514 19.1432ZM204.918 27.4138V25.2751L211.05 5.96709H216.868L223 25.2751V27.4138H218.558L217.481 23.1214H210.437L209.36 27.4138H204.918Z" fill="#FFFFFF"></path></svg>\n'

CSS = """.logo{height:20px;width:auto;display:block}a.brand{display:flex;align-items:center;gap:12px;text-decoration:none}a.brand span{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);border-left:1px solid var(--line);padding-left:12px}
.btn.red,button.red{background:#E31E30;border-color:#E31E30;color:#fff}.btn.red:hover,button.red:hover{background:#c81a2a}
form.access{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:24px}form.access label{display:flex;flex-direction:column;gap:6px;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
form.access .full{grid-column:1/-1}form.access input,form.access select,form.access textarea{font:15px/1.4 "Inter",Arial,sans-serif;color:#E8ECEF;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:0;padding:11px 12px;text-transform:none;letter-spacing:0}
form.access textarea{min-height:110px;resize:vertical}form.access input:focus,form.access select:focus,form.access textarea:focus{outline:none;border-color:#E31E30}form.access select option{background:#0E1216}
form.access button{font:600 14px "Inter",Arial,sans-serif;padding:13px 20px;border:1px solid #E31E30;cursor:pointer;justify-self:start}form.access .hp{position:absolute;left:-9999px}form.access p.note{grid-column:1/-1;margin:0;font-size:13px;color:var(--muted)}
@media (max-width:760px){form.access{grid-template-columns:1fr}a.brand span{display:none}header.top nav a:not([href$="#access"]){display:none}}"""


def header_brand(home):
    return f'<a class="brand" href="{home}" aria-label="CodeNinja Research home">{LOGO}<span>Research</span></a>'


def form(product="both"):
    sel = lambda v: " selected" if v == product else ""
    return f"""<form class="access" id="access-form" action="mailto:{INBOX}" method="post" enctype="text/plain">
<label>Name<input name="fullname" required autocomplete="name"></label>
<label>Work email<input name="email" type="email" required autocomplete="email"></label>
<label>Organization<input name="org" required autocomplete="organization"></label>
<label>Interested in<select name="product"><option value="Praxis"{sel("Praxis")}>Praxis</option><option value="Hyper Ontology"{sel("Hyper Ontology")}>Hyper Ontology</option><option value="Praxis and Hyper Ontology"{sel("both")}>Both (recommended)</option></select></label>
<label class="full">The operation you want to design or make living<textarea name="usecase" placeholder="For example: predict truck turn time at a container terminal, or stand up an ontology over our maintenance and ERP systems"></textarea></label>
<input class="hp" name="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="red" type="submit">Request beta access</button>
<p class="note">Opens your email app with the request addressed to {INBOX}; nothing is stored on this site. Prefer a form? Use the <a href="{PARENT}/contact">CodeNinja contact page</a>.</p>
</form>
<script>(function(){{var f=document.getElementById('access-form');if(!f)return;f.addEventListener('submit',function(e){{e.preventDefault();if(f.hp.value)return;
var p=f.product.value,b='Name: '+f.fullname.value+'\\nEmail: '+f.email.value+'\\nOrganization: '+f.org.value+'\\nInterested in: '+p+'\\n\\nOperation:\\n'+f.usecase.value+'\\n\\n(Sent from CodeNinja Research: '+location.href+')';
location.href='mailto:{INBOX}?subject='+encodeURIComponent('Beta access request: '+p+' ('+f.org.value+')')+'&body='+encodeURIComponent(b);}});}})();</script>"""


def footer_brand(home):
    return f'<a class="brand" href="{PARENT}" aria-label="CodeNinja">{LOGO}</a>'
