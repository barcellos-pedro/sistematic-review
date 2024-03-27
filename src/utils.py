prompt = """
Você é um professor de universidade que precisa fazer revisões sistemáticas de artigos para auxiliar alunos do ensino superior que estão se preparando para realizarem iniciação científica e/ou pesquisas.

Você irá receber o título e resumo (abstract) de um artigo e deverá responder se o artigo deve ser revisado ou não com base no objetivo da pesquisa e critérios de exclusão.

Caso o resumo do artigo não se enquadre em um dos resultados possíveis, marque a classificação como "n\a"

## Objetivo da pesquisa

Métodos, dificuldades ou analises do Ensino de linguagens de programação/logica de programação pra iniciantes adultos (não pode ser de crianças nem adolescentes)

## Possíveis resultados/classificações

- Sim
- Não
- Talvez

## Critérios de exclusão

- Trabalhos não disponíveis para leitura completa (download ou online)

- Artigos com o  mesmo  autor,  resumo,  data  de  publicação

- Como nossa análise está centrada em um revisão sistemática, os estudos com a mesma finalidade deverão ser excluídos

- Investigações que sejam educacionais, mas de áreas diferentes do foco de análise

- Investigações que sejam somente tecnicos, mas não abordem tópicos educacionais

- Estudos relacionados ao ensino de programação na Educação Infantil ou fundamental 1 e 2

- Artigos escritos de 2014 a 2024

- Linguagens de programação existentes atualmente

- Não ser artigo de inteligencia artificial

- Não ser relacionado a saúde

- Não ser uma revisão sistematica

- Trabalhos que foram resutados ou comprovadamente incorretos
"""

source_code = """

<!DOCTYPE html>


<APM_DO_NOT_TOUCH>

<script type="text/javascript">
(function(){
window.nVMV=!!window.nVMV;try{(function(){(function(){var a=-1;a={A:++a,cc:"false"[a],a:++a,Ha:"false"[a],K:++a,$e:"[object Object]"[a],cb:(a[a]+"")[a],Ja:++a,bb:"true"[a],D:++a,M:++a,dc:"[object Object]"[a],o:++a,U:++a,sj:++a,rj:++a};try{a.Ga=(a.Ga=a+"")[a.M]+(a.wa=a.Ga[a.a])+(a.bc=(a.va+"")[a.a])+(!a+"")[a.Ja]+(a.xa=a.Ga[a.o])+(a.va="true"[a.a])+(a.fb="true"[a.K])+a.Ga[a.M]+a.xa+a.wa+a.va,a.bc=a.va+"true"[a.Ja]+a.xa+a.fb+a.va+a.bc,a.va=a.A[a.Ga][a.Ga],a.va(a.va(a.bc+'"\\'+a.a+a.M+a.a+a.cc+"\\"+a.D+a.A+"("+a.xa+"\\"+a.a+a.U+a.a+"\\"+a.a+
a.o+a.A+a.bb+a.wa+a.cc+"\\"+a.D+a.A+"\\"+a.a+a.o+a.U+"\\"+a.a+a.M+a.a+"\\"+a.a+a.M+a.o+a.cb+a.wa+"\\"+a.a+a.o+a.U+"['\\"+a.a+a.o+a.A+a.Ha+"\\"+a.a+a.U+a.a+"false"[a.K]+a.wa+a.Ha+a.cb+"']\\"+a.D+a.A+"===\\"+a.D+a.A+"'\\"+a.a+a.o+a.Ja+a.xa+"\\"+a.a+a.o+a.K+"\\"+a.a+a.M+a.a+"\\"+a.a+a.M+a.o+"\\"+a.a+a.D+a.U+"')\\"+a.D+a.A+"{\\"+a.a+a.K+"\\"+a.a+a.a+"\\"+a.a+a.o+a.o+a.Ha+"\\"+a.a+a.o+a.K+"\\"+a.D+a.A+a.bb+a.cb+"\\"+a.a+a.o+a.o+a.dc+"\\"+a.a+a.U+a.a+a.fb+"\\"+a.a+a.M+a.K+"\\"+a.a+a.M+a.Ja+"\\"+a.a+a.o+
a.A+"\\"+a.D+a.A+"=\\"+a.D+a.A+"\\"+a.a+a.o+a.U+"\\"+a.a+a.M+a.a+"\\"+a.a+a.M+a.o+a.cb+a.wa+"\\"+a.a+a.o+a.U+"['\\"+a.a+a.o+a.A+a.Ha+"\\"+a.a+a.U+a.a+"false"[a.K]+a.wa+a.Ha+a.cb+"'].\\"+a.a+a.o+a.K+a.bb+"\\"+a.a+a.o+a.A+"false"[a.K]+a.Ha+a.dc+a.bb+"(/.{"+a.a+","+a.D+"}/\\"+a.a+a.D+a.U+",\\"+a.D+a.A+a.cc+a.fb+"\\"+a.a+a.M+a.o+a.dc+a.xa+"\\"+a.a+a.M+a.a+a.wa+"\\"+a.a+a.M+a.o+"\\"+a.D+a.A+"(\\"+a.a+a.U+a.A+")\\"+a.D+a.A+"{\\"+a.a+a.K+"\\"+a.a+a.a+"\\"+a.a+a.a+"\\"+a.a+a.a+"\\"+a.a+a.o+a.K+a.bb+a.xa+
a.fb+"\\"+a.a+a.o+a.K+"\\"+a.a+a.M+a.o+"\\"+a.D+a.A+"(\\"+a.a+a.U+a.A+"\\"+a.D+a.A+"+\\"+a.D+a.A+"\\"+a.a+a.U+a.A+").\\"+a.a+a.o+a.Ja+a.fb+a.$e+"\\"+a.a+a.o+a.Ja+a.xa+"\\"+a.a+a.o+a.K+"("+a.K+",\\"+a.D+a.A+a.D+")\\"+a.a+a.K+"\\"+a.a+a.a+"\\"+a.a+a.a+"});\\"+a.a+a.K+"}\\"+a.a+a.K+'"')())()}catch(d){a%=5}})();var b=24;
try{var ba,ca,oa=c(542)?1:0,ra=c(493)?1:0,sa=c(194)?1:0,ua=c(194)?1:0,xa=c(980)?0:1,za=c(498)?1:0;for(var Aa=(c(693),0);Aa<ca;++Aa)oa+=c(94)?2:1,ra+=c(669)?2:1,sa+=c(228)?2:1,ua+=(c(974),2),xa+=c(781)?1:2,za+=c(867)?2:3;ba=oa+ra+sa+ua+xa+za;window.eb===ba&&(window.eb=++ba)}catch(a){window.eb=ba}var e=!0;function f(a){var d=arguments.length,g=[];for(var h=1;h<d;h++)g[h-1]=arguments[h]-a;return String.fromCharCode.apply(String,g)}
function Ca(a){var d=62;a&&(document[q(d,180,167,177,167,160,167,170,167,178,183,145,178,159,178,163)]&&document[f(d,180,167,177,167,160,167,170,167,178,183,145,178,159,178,163)]!==t(68616527604,d)||(e=!1));return e}function t(a,d){a+=d;return a.toString(36)}function Da(){}Ca(window[Da[t(1086830,b)]]===Da);Ca(typeof ie9rgb4!==t(1242178186175,b));Ca(RegExp("\x3c")[t(1372181,b)](function(){return"\x3c"})&!RegExp(t(42865,b))[t(1372181,b)](function(){return"'x3'+'d';"}));
var Ea=window[q(b,121,140,140,121,123,128,93,142,125,134,140)]||RegExp(q(b,133,135,122,129,148,121,134,124,138,135,129,124),t(-6,b))[t(1372181,b)](window["\x6e\x61vi\x67a\x74\x6f\x72"]["\x75\x73e\x72A\x67\x65\x6et"]),Ha=+new Date+(c(712)?6E5:811649),Ia,Ja,Ka,La=window[f(b,139,125,140,108,129,133,125,135,141,140)],Na=Ea?c(548)?3E4:33773:c(450)?6E3:3232;
document[q(b,121,124,124,93,142,125,134,140,100,129,139,140,125,134,125,138)]&&document[f(b,121,124,124,93,142,125,134,140,100,129,139,140,125,134,125,138)](f(b,142,129,139,129,122,129,132,129,140,145,123,128,121,134,127,125),function(a){var d=94;document[f(d,212,199,209,199,192,199,202,199,210,215,177,210,191,210,195)]&&(document[q(d,212,199,209,199,192,199,202,199,210,215,177,210,191,210,195)]===t(1058781889,d)&&a[q(d,199,209,178,208,211,209,210,195,194)]?Ka=!0:document[q(d,212,199,209,199,192,
199,202,199,210,215,177,210,191,210,195)]===t(68616527572,d)&&(Ia=+new Date,Ka=!1,A()))});function q(a){var d=arguments.length,g=[];for(var h=1;h<d;++h)g.push(arguments[h]-a);return String.fromCharCode.apply(String,g)}function A(){if(!document[q(96,209,213,197,210,217,179,197,204,197,195,212,207,210)])return!0;var a=+new Date;if(a>Ha&&(c(421)?6E5:487184)>a-Ia)return Ca(!1);var d=Ca(Ja&&!Ka&&Ia+Na<a);Ia=a;Ja||(Ja=!0,La(function(){Ja=!1},c(704)?1:0));return d}A();
var Oa=[c(797)?21483786:17795081,c(368)?27611931586:2147483647,c(760)?1085017737:1558153217];function Pa(a){var d=45;a=typeof a===t(1743045631,d)?a:a[f(d,161,156,128,161,159,150,155,148)](c(577)?36:34);var g=window[a];if(!g||!g[f(d,161,156,128,161,159,150,155,148)])return;var h=""+g;window[a]=function(k,l){Ja=!1;return g(k,l)};window[a][f(d,161,156,128,161,159,150,155,148)]=function(){return h}}for(var Sa=(c(72),0);Sa<Oa[t(1294399181,b)];++Sa)Pa(Oa[Sa]);Ca(!1!==window[f(b,134,110,101,110)]);
window.Ra=window.Ra||{};window.Ra.mc="08dd70d6d8194000e347e4d781942d975ba48aad4eaab221b9e7dde34ea6e640a0cf5e79bb976f6c78028128b900db6544f14f38190f5bd3ff4ce3fc8b5171403c3e8f1ea5efefa9";function B(a){var d=+new Date;if(!document[f(82,195,199,183,196,203,165,183,190,183,181,198,193,196,147,190,190)]||d>Ha&&(c(176)?6E5:390330)>d-Ia)var g=Ca(!1);else g=Ca(Ja&&!Ka&&Ia+Na<d),Ia=d,Ja||(Ja=!0,La(function(){Ja=!1},c(147)?1:0));return!(arguments[a]^g)}function c(a){return 715>a}(function(a){a||setTimeout(function(){var d=setTimeout(function(){},250);for(var g=0;g<=d;++g)clearTimeout(g)},500)})(!0);})();}catch(x){}finally{ie9rgb4=void(0);};function ie9rgb4(a,b){return a>>b>>0};

})();

</script>
</APM_DO_NOT_TOUCH>

<script type="text/javascript" src="/TSPD/0807dc117eab200041ea4ba3f2079a31e4aab78269d9147b1308dc50f0f81b4036157592cbb292a6?type=9"></script>
<script type="text/javascript">

var home = {	
			metadata:{
				searchCount: '6,264,223',
				logoRelPath: '/xploreAssets/images/customer_logos/',
				thirdParthAuth: false,
				currentPage:  'document',
				xploreVirtual:'https://ieeexplore.ieee.org',
				isWebAccount: false,
				isProvisioned: false,				
				globalNotification:{},
				cart: {
						count: 0
				}
			}						
		};
		





		
</script>

<html lang="en-US">
	<head>
		<link rel="icon" type="image/x-icon" href="/assets/img/favicon.ico">
	    <meta name="google-site-verification" content="qibYCgIKpiVF_VVjPYutgStwKn-0-KBB6Gw4Fc57FZg" />
					
						
				
					
			 
			
				
		<meta name="Description" id="meta-description" content="This paper involves a limit cycle oscillator-frequency lock loop (LCO-FLL) based control algorithm for unified power quality controllers-S type (UPQC-S) for com">
		
		<link rel="canonical" href="https://ieeexplore.ieee.org/document/9056993" /> 
		
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		
		<!-- Disable "click" touch event 300ms delay for Chrome/Firefox on Android -->
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		
		




		<meta name="parsely-title" content="Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains | CSEE Journals &amp; Magazine | IEEE Xplore" />


		<meta name="parsely-link" content="https://ieeexplore.ieee.org/document/9056993" />


	
		<meta name="parsely-type" content="post" />
	
	


		<meta name="parsely-section" content="Journals" />


		<meta name="parsely-author" content="Sabha Raj Arya" />

		<meta name="parsely-author" content="Sayed Javed Alam" />

		<meta name="parsely-author" content="Papia Ray" />


		<title>Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains | CSEE Journals &amp; Magazine | IEEE Xplore</title>
		
    <meta name="bingbot" content="nocache"> 
	
		
			<meta property="twitter:title" content="Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains" />
			<meta property="og:title" content="Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains" />
		
		
			<meta property="twitter:description" content="This paper involves a limit cycle oscillator-frequency lock loop (LCO-FLL) based control algorithm for unified power quality controllers-S type (UPQC-S) for compensation of reactive power, to maintain a unity power factor, regulate constant voltage at the PCC, mitigate sag, swell and to eliminate harmonics. In this approach, an extraction of fundamental in-phase and quadrature components for the estimation of reference signals are taken from the LCO-FLL circuit. The control LCO-FLL provides a high grade of protection against sag-swell voltages, unbalance loading and harmonics present in the utility grid. In addition to that, it has advantageous characteristics of synchronization with the grid frequency at any previously mentioned conditions without use of phase locked loops or trigonometric functions. Other advantages of the LCO-FLL are to give useful information to estimate fundamental components from a highly polluted grid scenario. The values obtained from the JAYA optimization algorithm are used to fine-tune the proportional integral (PI) controller gains, so that it maintains DC link voltage to the desired level. The mean square error (MSE) is employed as an objective function for optimizing the error between actual and reference values. The control algorithm based on LCO-FLL is developed in MATLAB/Simulink software and it is tested for power conditioning features ." />
			<meta property="og:description" content="This paper involves a limit cycle oscillator-frequency lock loop (LCO-FLL) based control algorithm for unified power quality controllers-S type (UPQC-S) for compensation of reactive power, to maintain a unity power factor, regulate constant voltage at the PCC, mitigate sag, swell and to eliminate harmonics. In this approach, an extraction of fundamental in-phase and quadrature components for the estimation of reference signals are taken from the LCO-FLL circuit. The control LCO-FLL provides a high grade of protection against sag-swell voltages, unbalance loading and harmonics present in the utility grid. In addition to that, it has advantageous characteristics of synchronization with the grid frequency at any previously mentioned conditions without use of phase locked loops or trigonometric functions. Other advantages of the LCO-FLL are to give useful information to estimate fundamental components from a highly polluted grid scenario. The values obtained from the JAYA optimization algorithm are used to fine-tune the proportional integral (PI) controller gains, so that it maintains DC link voltage to the desired level. The mean square error (MSE) is employed as an objective function for optimizing the error between actual and reference values. The control algorithm based on LCO-FLL is developed in MATLAB/Simulink software and it is tested for power conditioning features ." />
		
		
		
  		
			<meta name="twitter:card" content="summary" />
 			<meta property="twitter:image" content="https://ieeexplore.ieee.org/assets/img/ieee_logo_smedia_200X200.png" />
			<meta property="og:image" content="https://ieeexplore.ieee.org/assets/img/ieee_logo_smedia_200X200.png" />
  		
		
						 	
	
	

		





	
		<script src="https://cmp.osano.com/AzyzptTmRlqVd2LRf/6fda1518-2a1e-4b5b-a049-da0bef71dcab/osano.js"></script>
		<link rel="stylesheet" href="https://cookie-consent.ieee.org/ieee-cookie-banner.css" type="text/css"/>
	
	
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge">






<g:compress>
	<link rel="stylesheet" href="/assets/css/simplePassMeter.min.css?cv=20240305_000000" />
	<link rel="stylesheet" type="text/css" media="screen, print" href="/assets/dist/ng-new/styles.css?cv=20240305_000000"/>
	<link rel="stylesheet" type="text/css" media="screen, print" href="/assets/dist/ng-new/customStyles.css?cv=20240305_000000"/>
	<link rel="stylesheet" href="/assets/vendor/swiper/dist/idangerous.swiper.css?cv=20240305_000000">
	<link rel="stylesheet" type="text/css" media="screen, print" href="/assets/css/jquery-ui-1.8.19.custom.css?cv=20240305_000000"/>
</g:compress>




		

	<script type='text/javascript'>
		var googletag = googletag || {};
		googletag.cmd = googletag.cmd || [];
		(function() {
		var gads = document.createElement('script');
		gads.async = true;
		gads.type = 'text/javascript';
		var useSSL = 'https:' == document.location.protocol;
		gads.src = (useSSL ? 'https:' : 'http:') + 
		'//securepubads.g.doubleclick.net/tag/js/gpt.js';
		var node = document.getElementsByTagName('script')[0];
		node.parentNode.insertBefore(gads, node);
		})();
	</script>

		<script type="text/javascript" src="/assets/vendor/jquery/jquery-3.5.1.min.js?cv=20240305_000000" charset="utf-8"></script>
		
	</head>
	<body class="body-resp">

		<div id="global-notification" class="row stats-global-notification">
			<div class="hide u-hide-important col Notification Notification--global Notification--fixed">
				<a href class="Notification-close js-close" aria-label="close message button"><i class="fa fa-close"></i></a>
				<div class="Notification-header"></div>
				<div class="Notification-text"></div>
			</div>
		</div>

		<div id="LayoutWrapper">
				<div class="row">
					<div class="col">
						







<div class="Header" id="xplore-header" data-service="true" data-inst="false" data-web="false" style="display:none"></div>



						<div id="global-alert-message"></div>
						








<meta name="cToken" content="eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqqVkosKFCyUoooyMkvSlXSUcosLgZyK2Dc1AqgrKG5oaGpuYG5hQFQPrEEKmBmYWBhUAsAAAD__w.RGAHekX6hBvEuGbj5zfaS17MWPvtpeJRDrESfxcXDIlWdPgOAGgejwXxwAbHQMDVzz3jgaeGk8WYIiCCSdpVFA">

<script type="text/javascript">
	
	
	
	document.write('<base href="/document/" />');
	
	
</script>

<!-- XPL-21560-Added as part of Universal CASA-Dev -->
<script type="text/javascript" src="https://scholar.google.com/scholar_js/casa.js" async></script>

<script type="text/javascript" src="https://app.cadmoremedia.com/Scripts/Embed.js"></script>
<!--- This is a picture popup embed for mobilew view.  -->
<script type="text/javascript" src="https://app.cadmoremedia.com/Scripts/PicturePop.js"></script>







<script type="text/javascript">
var body_rightsLink ="", body_publisher = "";
var recordId = "";


var AUTHOR_PROFILE = 'ON';
if (AUTHOR_PROFILE.toUpperCase() == "OFF"){
	var AUTHOR_PROFILE_ENABLED = false;
}else{
	var AUTHOR_PROFILE_ENABLED = true;
}

var xplGlobal = {
	document: {
		disqus:{
			remote_auth_s3 : '',
			public_api_key:'1lxKgMbpNIbQvfk2tqLcWeSVloE8rgIY2CV1tCu3Vp641oL4eEITYBbkViJJGNYY',
			short_name:'ieeexplore',
			client_url:'https://ieeexplore.ieee.org',
			sso_enabled:'{$sessionProfile.provisioned}'
		},

		fullTextAccess: false,
		isAccessFromInstitution: false
		
	}
};
	
	xplGlobal.document.metadata={"userInfo":{"institute":false,"member":false,"individual":false,"guest":false,"subscribedContent":false,"fileCabinetContent":false,"fileCabinetUser":false,"institutionalFileCabinetUser":false,"showPatentCitations":true,"showGet802Link":false,"showOpenUrlLink":false,"tracked":false,"delegatedAdmin":false,"desktop":false,"isInstitutionDashboardEnabled":false,"isInstitutionProfileEnabled":false,"isRoamingEnabled":false,"isDelegatedAdmin":false,"isMdl":false,"isCwg":false,"isAcademic":false,"isIel":false},"authors":[{"name":"Sabha Raj Arya","affiliation":["Department of Electrical Engineering, Sardar Vallabhai National Institute of Technology, Surat, India"],"firstName":"Sabha Raj","lastName":"Arya"},{"name":"Sayed Javed Alam","affiliation":["Department of Electrical Engineering, Sardar Vallabhai National Institute of Technology, Surat, India"],"firstName":"Sayed Javed","lastName":"Alam"},{"name":"Papia Ray","affiliation":["Department of Electrical Engineering, Veer Surendra Sai University of Technology, Sambalpur, India"],"firstName":"Papia","lastName":"Ray"}],"issn":[{"format":"Electronic ISSN","value":"2096-0042"}],"articleNumber":"9056993","dbTime":"3 ms","metrics":{"wosCitationCount":0,"citationCountPaper":0,"citationCountPatent":0,"totalDownloads":580},"purchaseOptions":{"showOtherFormatPricingTab":false,"showPdfFormatPricingTab":true,"pdfPricingInfoAvailable":false,"otherPricingInfoAvailable":false,"mandatoryBundle":false,"optionalBundle":false,"displayTextWhenPdfPricingNotAvailable":"The purchase and pricing options for this item are unavailable. Select items are only available as part of a subscription package. You may try again later or <a href='https://ieeexplore.ieee.org/xpl/contact' target='_blank'>contact us</a> for more information.","displayTextWhenOtherFormatPricingNotAvailable":"The purchase and pricing options for this item are unavailable. Select items are only available as part of a subscription package. You may try again later or <a href='https://ieeexplore.ieee.org/xpl/contact' target='_blank'>contact us</a> for more information."},"getProgramTermsAccepted":false,"sections":{"abstract":"true","authors":"true","figures":"false","multimedia":"false","references":"false","citedby":"false","keywords":"true","definitions":"false","algorithm":"false","dataset":"false","cadmore":"false","footnotes":"false","disclaimer":"false","relatedContent":"false","metrics":"true"},"publicationTitle":"CSEE Journal of Power and Energy Systems","abstract":"This paper involves a limit cycle oscillator-frequency lock loop (LCO-FLL) based control algorithm for unified power quality controllers-S type (UPQC-S) for compensation of reactive power, to maintain a unity power factor, regulate constant voltage at the PCC, mitigate sag, swell and to eliminate harmonics. In this approach, an extraction of fundamental in-phase and quadrature components for the estimation of reference signals are taken from the LCO-FLL circuit. The control LCO-FLL provides a high grade of protection against sag-swell voltages, unbalance loading and harmonics present in the utility grid. In addition to that, it has advantageous characteristics of synchronization with the grid frequency at any previously mentioned conditions without use of phase locked loops or trigonometric functions. Other advantages of the LCO-FLL are to give useful information to estimate fundamental components from a highly polluted grid scenario. The values obtained from the JAYA optimization algorithm are used to fine-tune the proportional integral (PI) controller gains, so that it maintains DC link voltage to the desired level. The mean square error (MSE) is employed as an objective function for optimizing the error between actual and reference values. The control algorithm based on LCO-FLL is developed in MATLAB/Simulink software and it is tested for power conditioning features .","displayPublicationDate":"06 April 2020","dateOfInsertion":"06 April 2020","publicationDate":"September 2020","publicationYear":"2020","pdfPath":"/iel7/7054730/9160441/09056993.pdf","doi":"10.17775/CSEEJPES.2019.01030","formulaStrippedArticleTitle":"Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains","displayPublicationTitle":"CSEE Journal of Power and Energy Systems","startPage":"649","endPage":"661","pdfUrl":"/stamp/stamp.jsp?tp=&arnumber=9056993","keywords":[{"type":"IEEE Keywords","kwd":["Voltage control","Power quality","Optimization","Reactive power","Phase locked loops","Perturbation methods","Frequency locked loops"]},{"type":"Author Keywords","kwd":["JAYA","MSE","LCO-FLL","PI Tuning","Sag","unbalanced","VSC"]}],"pubLink":"/xpl/RecentIssue.jsp?punumber=7054730","issueLink":"/xpl/tocresult.jsp?isnumber=9160441&punumber=7054730","doiLink":"https://doi.org/10.17775/CSEEJPES.2019.01030","allowComments":false,"authorNames":"Sabha Raj Arya;Sayed Javed Alam;Papia Ray","isGetAddressInfoCaptured":false,"isMarketingOptIn":false,"pubTopics":[{"name":"Power, Energy and Industry Applications"}],"publisher":"CSEE","displayDocTitle":"Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains","isDynamicHtml":false,"isSpringer":false,"volume":"6","issue":"3","isJournal":true,"isFreeDocument":true,"xploreDocumentType":"Journals & Magazine","isChapter":false,"isProduct":false,"isStandard":false,"isEarlyAccess":false,"isOpenAccess":true,"isEphemera":false,"isConference":false,"isPromo":false,"isBookWithoutChapters":false,"isBook":false,"htmlAbstractLink":"/document/9056993/","isNow":false,"persistentLink":"https://ieeexplore.ieee.org/servlet/opac?punumber=7054730","isCustomDenial":false,"isSAE":false,"isOUP":false,"isSMPTE":false,"startPage":"649","openAccessFlag":"T","insertDate":"06 April 2020","ephemeraFlag":"false","title":"Control algorithm based on limit cycle oscillator-FLL for UPQC-S with optimized PI gains","html_flag":"false","ml_html_flag":"false","sourcePdf":"18JPES20190103.pdf","displayPublicationDate":"06 April 2020","mlTime":"PT0.026459S","pdfPath":"/iel7/7054730/9160441/09056993.pdf","sponsors":[{"name":"Chinese Society of Electrical Engineering","url":""}],"isNumber":"9160441","contentType":"periodicals","publicationDate":"September 2020","publicationNumber":"7054730","citationCount":"0","issue":"3","articleId":"9056993","publicationTitle":"CSEE Journal of Power and Energy Systems","sections":{"abstract":"true","authors":"true","figures":"false","multimedia":"false","references":"false","citedby":"false","keywords":"true","definitions":"false","algorithm":"false","dataset":"false","cadmore":"false","footnotes":"false","disclaimer":"false","relatedContent":"false","metrics":"true"},"volume":"6","contentTypeDisplay":"Journals","publicationYear":"2020","subType":"CSEE","lastupdate":"2024-03-09","mediaPath":"","endPage":"661","displayPublicationTitle":"CSEE Journal of Power and Energy Systems","doi":"10.17775/CSEEJPES.2019.01030"};








</script>



<div class="ng2-app">
	
	
		<!-- <xpl-searchbar show-count="false"></xpl-searchbar> -->
	
	<div class="global-content-wrapper">
		<xpl-root>
			<div class="Spinner"></div>
		</xpl-root>
	</div>
	
	<!-- START: Angular 2+ Migration: Due to Angualr2+ migration AngualrJs router place holder commented -->
<!-- 	<div ng-show="stateIsLoading" class="Spinner"></div>
	<div ui-view class="{{stateIsLoading ? 'loading': ''}}"
		autoscroll="false"></div>
 -->	<!-- END: Angular 2+ Migration-->
</div>

						




<section id="xploreFooter">
	
	<div class="Footer stats-footer hide-mobile">
		<div class="pure-g Footer-sections">
			<div class="pure-u-1-4">
				<h3 class="Footer-header">IEEE Account</h3>
				<ul class="Footer-list">
					<li><a href="https://www.ieee.org/profile/changeusrpwd/showChangeUsrPwdPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Change Username/Password</a></li>
					<li><a href="https://www.ieee.org/profile/address/getAddrInfoPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Update Address</a></li>
				</ul>
			</div>
			<div class="pure-u-1-4">
				<h3 class="Footer-header">Purchase Details</h3>
				<ul class="Footer-list">
					<li><a href="https://www.ieee.org/profile/payment/showPaymentHome.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Payment Options</a></li>
					<li><a href="https://www.ieee.org/profile/vieworder/showOrderHistory.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Order History</a></li>
					<li><a href="/articleSale/purchaseHistory.jsp">View Purchased Documents</a></li>
				</ul>
			</div>
			<div class="pure-u-1-4">
				<h3 class="Footer-header">Profile Information</h3>
				<ul class="Footer-list">
					<li><a href="https://www.ieee.org/ieee-privacyportal/app/ibp?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Communications Preferences</a></li>
					<li><a href="https://www.ieee.org/profile/profedu/getProfEduInformation.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Profession and Education</a></li>
					<li><a href="https://www.ieee.org/profile/tips/getTipsInfo.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore">Technical Interests</a></li>
				</ul>
			</div>
			<div class="pure-u-1-4">
				<h3 class="Footer-header">Need Help?</h3>
				<ul class="Footer-list">
					<li><strong>US &amp; Canada:</strong> +1 800 678 4333</li>
					<li><strong>Worldwide: </strong> +1 732 981 0060<br>
					</li>
					<li><a href="/xpl/contact">Contact &amp; Support</a></li>
				</ul>
			</div>
		</div>
		<div class="row">
			<div class="col-12 Footer-bottom">
				<div class="Footer-bottom-inner-div row">
					<div class="col">
						<ul class="Menu Menu--horizontal Menu--dividers u-mb-1">
							<li class="Menu-item"><a href="/Xplorehelp/about-ieee-xplore.html">About IEEE <em>Xplore</em></a></li>
							<li class="Menu-item"><a href="/xpl/contact">Contact Us</a></li>
							<li class="Menu-item"><a href="/Xplorehelp/Help_start.html" target="blank">Help</a></li>
							<li class="Menu-item"><a href="/Xplorehelp/accessibility-statement.html" target="blank">Accessibility</a></li> 
							<li class="Menu-item"><a href="/Xplorehelp/Help_Terms_of_Use.html" target="_blank">Terms of Use</a></li>
							<li class="Menu-item"><a href="http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html">Nondiscrimination Policy</a></li>
							<li class="Menu-item"><a href="/xpl/sitemap.jsp">Sitemap</a></li>
							<li class="Menu-item"><a href="http://www.ieee.org/about/help/security_privacy.html" target="blank">Privacy &amp; Opting Out of Cookies</a></li>
						</ul>
						<p class="Footer-bottom-terms">
							A not-for-profit organization, IEEE is the world's largest technical professional organization dedicated to advancing technology for the benefit of humanity.<br>&copy; Copyright 2024 IEEE - All rights reserved. Use of this web site signifies your agreement to the terms and conditions.
						</p>
					</div>

					<div><i class="logo-ieee-white"></i></div>
				</div>
				
			</div>
		</div>
	</div>

	
	
</section>

						<!-- BEGIN: tealium in v2/common/template.jsp. We need to include tealiumAnalytics.js here since Angular 2+ app load if you load after commnon.js then tealium value will not be available in angular 2+ app  -->
						






		<!-- BEGIN: TealiumAnalytics.jsp -->
		
		
		
		
		
		
		
		
		
		
		
		
			
				
			
			
			
			
		
		
		
		
		
		

			<script type ="text/javascript">
 				// tealium config vars
				var TEALIUM_CONFIG_TAGGING_ENABLED = true;		
				var TEALIUM_CONFIG_CDN_URL = '//tags.tiqcdn.com/utag/';
				var TEALIUM_CONFIG_ACCOUNT_PROFILE_ENV = 'ieeexplore/main/prod';
				
				// tealium utag_data values for user 
				var TEALIUM_userType = 'Anonymous';
				var TEALIUM_userInstitutionId = '';
				var TEALIUM_userId = '';
				var TEALIUM_user_third_party = '';
				
				var TEALIUM_products = '';
			</script>


			<script type="text/javascript">
			// asynchronously load tealium's utag.js , which declares tealium JS variables like; utag_data, utag
			(function(a,b,c,d){
			
				a=TEALIUM_CONFIG_CDN_URL + TEALIUM_CONFIG_ACCOUNT_PROFILE_ENV + '/utag.js';
				b=document;c='script';d=b.createElement(c);d.src=a;
				d.type='text/java'+c;d.async=true;
				a=b.getElementsByTagName(c)[0];a.parentNode.insertBefore(d,a);
			})();
			</script>

			<script type="text/javascript" src="/assets/dist/js/analytics/tealiumTagsData.js?cv=20240305_000000"></script>
			<script type="text/javascript" src="/assets/dist/js/analytics/tealiumAnalytics.js?cv=20240305_000000"></script>


		
 		
		<!-- END: TealiumAnalytics.jsp -->
			 

						<!-- END: tealium in v2/common/template.jsp -->
						






	
	

<script type="text/javascript" src="/xploreAssets/MathJax-274/MathJax.js?config=default"></script>














<link rel="stylesheet" href="/assets/css/ie7Sniffer.css?cv=20240305_000000">
<script type="text/javascript" src="/assets/vendor/js-cookie/src/js.cookie.js?cv=20240305_000000"></script>



	<script type="text/javascript" src="/assets/vendor/fingerprintjs2/fingerprint2.js?cv=20240305_000000"></script>
	<script type="text/javascript" src="/assets/dist/js/fingerprint/fingerprint.js?cv=20240305_000000"></script>


<!-- START OF Angular bundle assets -->
<script type="text/javascript" src='/assets/dist/ng-new/runtime.js?cv=20240305_000000' defer charset="utf-8"></script>
<script type="text/javascript" src='/assets/dist/ng-new/polyfills.js?cv=20240305_000000' defer charset="utf-8"></script>

<script type="text/javascript" src='/assets/dist/ng-new/main.js?cv=20240305_000000' defer charset="utf-8"></script>
<!-- END OF Angular bundle assets -->

<!-- Usabilla Combicode for IEEE-->
<!-- Begin Usabilla for Websites embed code -->
<script type="text/javascript">/*{literal}<![CDATA[*/window.lightningjs||function(c){function g(b,d){d&&(d+=(//.test(d)?"&":"?")+"lv=1");c[b]||function(){var i=window,h=document,j=b,g=h.location.protocol,l="load",k=0;(function(){function b(){a.P(l);a.w=1;c[j]("_load")}c[j]=function(){function m(){m.id=e;return c[j].apply(m,arguments)}var b,e=++k;b=this&&this!=i?this.id||0:0;(a.s=a.s||[]).push([e,b,arguments]);m.then=function(b,c,h){var d=a.fh[e]=a.fh[e]||[],j=a.eh[e]=a.eh[e]||[],f=a.ph[e]=a.ph[e]||[];b&&d.push(b);c&&j.push(c);h&&f.push(h);return m};return m};var a=c[j]._={};a.fh={};a.eh={};a.ph={};a.l=d?d.replace((g=="https:"?g:"http:")+"//"):d;a.p={0:+new Date};a.P=function(b){a.p[b]=new Date-a.p[0]};a.w&&b();i.addEventListener?i.addEventListener(l,b,!1):i.attachEvent("on"+l,b);var q=function(){function b(){return["<head></head><",c,' onload="var d=',n,";d.getElementsByTagName('head')[0].",d,"(d.",g,"('script')).",i,"='",a.l,"'\"></",c,">"].join("")}var c="body",e=h[c];if(!e)return setTimeout(q,100);a.P(1);var d="appendChild",g="createElement",i="src",k=h[g]("div"),l=k[d](h[g]("div")),f=h[g]("iframe"),n="document",p;k.style.display="none";e.insertBefore(k,e.firstChild).id=o+"-"+j;f.frameBorder="0";f.id=o+"-frame-"+j;/MSIE[ ]+6/.test(navigator.userAgent)&&(f[i]="javascript:false");f.allowTransparency="true";l[d](f);try{f.contentWindow[n].open()}catch(s){a.domain=h.domain,p="javascript:var d="+n+".open();d.domain='"+h.domain+"';",f[i]=p+"void(0);"}try{var r=f.contentWindow[n];r.write(b());r.close()}catch(t) { f[i]=p+'d.write("'+b().replace(/"/g,String.fromCharCode(92)+'"')+'");d.close();'}a.P(2)}; a.l&&setTimeout(q,0)})()}();c[b].lv="1";return c[b]}var o="lightningjs",k=window[o]=g(o);k.require=g;k.modules=c}({}); if(!navigator.userAgent.match(/Android|BlackBerry|BB10|iPhone|iPad|iPod|Opera Mini|IEMobile/i)) {window.usabilla_live = lightningjs.require("usabilla_live", "//w.usabilla.com/e9930a118e08.js"); } else {window.usabilla_live = lightningjs.require("usabilla_live", "//w.usabilla.com/118ca38ae742.js"); }/*]]>{/literal}*/</script>
<!-- end usabilla live embed code -->


<!-- START: Bombora tagging integration XPL-25079-->
<script type="text/javascript">
	(function (w,d,t) {
		_ml = w._ml || {};
		_ml.eid = '82420';
		var s, cd, tag; s = d.getElementsByTagName(t)[0]; cd = new Date();
		tag = d.createElement(t); tag.async = 1;
		tag.src = 'https://ml314.com/tag.aspx?' + cd.getDate() + cd.getMonth();
		s.parentNode.insertBefore(tag, s);
	})(window,document,'script');
</script>
<!-- END: Bombora Tagging Integration-->







	







<div style="width: 1263px;" id="popup_overlay"></div>

<g:compress>








		
		
			
				
					
					
								<script type="text/javascript" src='/assets/vendor/modernizr/modernizr.js?cv=20240305_000000' charset="utf-8"></script>
					
								
			
				
					
						








 

<script>
	var $j = jQuery.noConflict();
	var j$ = jQuery.noConflict();
	var membershipIncomplete;
    var IS_INDIVIDUAL_USER=false;

	var searchPropertiesParamQueryText = 'queryText';
	var searchPropertiesParamNewSearch = 'newsearch';
	var searchPropertiesParamMatchBoolean = 'matchBoolean';
	var searchPropertiesParamSearchWithin = 'searchWithin';
	var searchInterfaceArticleIndexTermReference = 'Search_Index_Terms';
	var searchPropertiesParamRecordsPerPage = 'rowsPerPage';
	var searchPropertiesParamPageNumber = 'pageNumber';
	var searchPropertiesParamRemoveRefinement = 'removeRefinement';	
	var searchPropertiesParamSearchField = 'searchField';
	var searchPropertiesParamArticleNumber = 'arnumber';
	
	var authorsGetDisplay = 'Authors';
	var authorsFirstNameProperty = 'First Name';
	var authorsLastNameProperty = 'Last Name';
	var authorsMiddleNameProperty = 'Middle Name';
	var pubTitleDispNameProperty = 'Publication Title';
	var volumeDispNameProperty = 'Volume';
	var issueDispNameProperty = 'Issue';
	var startPageDispNameProperty = 'Start Page';
	var endPageDispNameProperty = 'Start Page';

	var searchIcsTermProperty = 'Standards ICS Terms';
	var SearchMapperParamSearchField = 'searchField';
	
	var SearchMapperParamNewSearch = 'newsearch';
	var SearchMapperParamArticleNumber = 'arnumber';	
		
	
	
	var NTPT_IMAGE_LOCATION = '';
	var XPLORE_SSL_HOST = 'https://ieeexplore.ieee.org';	
	
	var SSL_YES_NO = 'yes';
	if (SSL_YES_NO.toUpperCase() == "NO"){
		var XPLORE_SSL_YES_NO = false;
	}else{
		var XPLORE_SSL_YES_NO = true;
	}
	var WEBSERVICES_SSL_YES_NO = 'yes';
	if (WEBSERVICES_SSL_YES_NO.toUpperCase() == "NO"){
		var XPLORE_WEBSERV_YES_NO = false;
	}else{
		var XPLORE_WEBSERV_YES_NO = true;
	}
	
	var AUTHOR_PROFILE = 'ON';
	if (AUTHOR_PROFILE.toUpperCase() == "OFF"){
		var AUTHOR_PROFILE_ENABLED = false;
	}else{
		var AUTHOR_PROFILE_ENABLED = true;
	}

	var IMAGE_SEARCH_FLAG = 'OFF';
	if (IMAGE_SEARCH_FLAG.toUpperCase() == "ON"){
		var IMAGE_SEARCH_ENABLED = true;
	} else {
		var IMAGE_SEARCH_ENABLED = false;
	}
	
	var ILN_ENABLED = true;
	
	
	var IBP_MEMBEER_SIGNIN_TIME_WAIT_IN_MILLIES = '2800';
	var ASSETS_RELATIVE_PATH = '/assets'; // NOTE: AngularJS code relies on this
	var ASSETS_RELATIVE_PATH_NO_SERVER = '/assets';
	var ASSETS_VERSION = '20240305_000000'; // NOTE: AngularJS code relies on this
	var IBP_WS_ASSETS='https://www.ieee.org';
	var IBP_WS_ENABLED_FLAG = true;
	var ENTERPRISE_CART_URL = 'https://www.ieee.org/cart/public/myCart/page.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE%20Xplore';
	var IEEE_USER_INFO_COOKIE = 'ieeeUserInfoCookie';
	
	var ACC_MGMT_NEW = true;
	if (! XPLORE_WEBSERV_YES_NO) {
		var ACC_MGMT_NEW = 'false';
	}
	var ACC_MGMT_CREATE_URL = 'https://www.ieee.org/profile/public/createwebaccount/showCreateAccount.html?ShowMGAMarkeatbilityOptIn=true&sourceCode=xplore&car=IEEE-Xplore&autoSignin=Y';
	var ACC_MGMT_FORGOT_PASSWD_URL = 'https://www.ieee.org/profile/public/forgotpassword/forgotUsernamePassword.html?sourceCode=xplore';

	var SPECIAL_CHARACTER_MAPS = '&:.AND.,=:.EQ.,+:.PLS.,#:.HSH.';
	var SPECIAL_CHARACTERS = new Array();
	var SPECIAL_CHARACTER_REPLACEMENTS = new Array();
	var characterMaps = SPECIAL_CHARACTER_MAPS.split(",");
	for (var i = 0; i < characterMaps.length; i++) {
		parts = characterMaps[i].split(":");
		SPECIAL_CHARACTERS[i] = parts[0];
		SPECIAL_CHARACTER_REPLACEMENTS[i] = parts[1];
	}

	var MAX_WILDCARDS = '9';
	var MAX_SEARCH_TERMS = '25';
	var ALL_SEARCH_FIELDS = 'Search_Index_Terms:Index Terms,Search_All_Text:Full Text & Metadata,Search_All:All Metadata,fullText:Full Text Only,Search_Publication_Title:Search Publication Title,Search_Related_Terms:Search Related Terms,Search_Authors:Author Name,Search_Standard_Ics_Title:ICE Terms,promoTopic:Custom Search,id:Article Number,moduleNumber:Module Number,part_num:Part_Num,issn:ISSN,isbn:ISBN,eisbn:EISBN,issueId:IS Number,pubIssueId:Pub Issue Id,accessionNumber:Accession Number,copyrightHolder:Copyright Holder,copyrightYear:Copyright Year,license:License,documentAbstract:Abstract,publicationId:Publication Number,parentPublicationId:Parent Publication Number,parentId:Parent Id,standardArticleId:Standard Article Id,title:Document Title,parentTitle:Parent Publication Title,parentDisplayTitle:Parent Display Title,publicationTitle:Publication Title,publicationDisplayTitle:Publication Display Title,volume:Volume,issue:Issue,paddedIssueNumber:Padded Issue Number,part:Part,startPage:Start Page,endPage:End Page,filePath:File Path,publicationDate:Publication Date,PublicationYear:Publication Year,onlineDate:Online Date,month:Month,Author:Author Pref Names,authorNormNames:Author Norm Names,author:Authors,authorIds:Author Ids,firstName:First Name,middleName:Middle Name,lastName:Last Name,authorAffiliations:Author Affiliations,authorBio:Author Bio,authorImg:Author Img,referenceCount:Reference Count,citationCount:Citation Count,downloadCount:Download Count,patentCount:Patent Count,multimediaFlag:Multimedia Flag,biomedicalEngFlag:Biomedical Eng Flag,nonIeee:Non IEEE,stdsProductNumber:STDS Product Number,bmsProductNumber:Bms Product Number,status:Status,doi:DOI,articleDoi:Article DOI,publicationDoi:Publication DOI,pdfPath:Pdf Path,pdfSize:Pdf Size,contentSubtype:Content Subtype,Publisher:Publisher,inspecControlledTerms:INSPEC Controlled Terms,ieeeTerms:IEEE Terms,unsiloTerms:Unsilo Terms,authorTerms:Author Keywords,maiTerms:MAI Terms,meshTerms:Mesh_Terms,pacsTerms:PACS Terms,insertDate:Insert Date,ConferenceLocation:Conference Location,indexContent:Index Content,coden:CODEN,documentText:Document Text,standardNumber:Standard Number,preprintFlag:Preprint Flag,rapidPostFlag:Rapid Post Flag,lastUpdate:Last Update,newFlag:New Flag,openAccessFlag:Open Access Flag,publicationOpenAccess:Publication Open Access,promoFlag:Promo Flag,pubmedId:Pubmed Id,duration:Duration,society:Society,conference:Conference,ConferenceCountry:ConferenceCountry,conferenceStartDate:Conference Start Date,conferenceEndDate:Conference End Date,societyUrl:Society URL,idSubject:Id Subject,bookNumber:Book Number,pages:Pages,editionNumber:Edition Number,sequence:Sequence,relatedInfoType:Related Info Type,relatedInfo:Related Info,formatIsbn:Format ISBN,meetingDate:Meeting Date,courseLevel:Course level,courseParts:Course Parts,courseId:Course ID,aboutUrl:About Url,additionalUrl:Additional Url,authorsUrl:Authors Url,openAccessUrl:Open Access Url,openAccessFlag:Open Access flag,partnumVendorurlMediatype:Partnum VendorURL MediaType,brandingImageFile:Branding Image File,coverImageFile:Cover Image File,latestIssueCoverImage:Latest Issue Cover Image,frequency:Frequency,fieldOfInterest:Field Of Interest,gParentPublicationNumber:G Parent Publication Number,msUrl:Ms Url,publicationRelationship:Relationship,societyImage:Society Image,visitUrl:Visit Url,visitWebsite:Visit Website,startYear:Start Year,endYear:End Year,publicationInactive:Publication Inactive,recordType:Record Type,picCodeDescription:Pic Code Description,picCode:Pic Code,sponsors:Sponsors,issueNotes:Notes,conferenceDate:Conference Date,publicationContact:Publication Contact,isbuyable:isBuyable,standardRelationships:Standard Relationships,unavailableForSale:Unavailable for Sale,availableForSale:Available for Sale,standardFamily:Standard Family,standardGroup:Standard Group,productUrl:Product Url,isbnMediatype:ISBN MediaType,htmlFlag:Html Flag,rightslinkFlag:Rightslink Flag,pageCount:Page Count,name:Name,tableOfContents:Table of Contents,timeStamp:Time Stamp,subTitle:Sub Title,relatedItem:Related Item,referenceMaterial:Reference Material,latestIssueTime:Latest Issue Time,startYear:First Published Year,insertDate:Search Latest Date,pbdFlag:Pbd Flag,lmsUrl:Lms Url,currentVolume:Current Volume,graphicalFile:Graphical File,graphicalCoverImage:Graphical Cover Image,graphicalSummary:Graphical Summary,graphicalType:Graphical Type,graphicalAbstractFile:Graphical Abstract File,graphicalAbstractImage:Graphical Abstract Image,graphicalAbstractType:Graphical Abstract Type,graphicalAbstractSummary:Graphical Abstract Summary,authorNativeNames:Native Name,externalId:Article Page Number,standardBundles:Standard Bundles,standardBundleParts:Standard Bundle Parts,virtualTitle:Virtual Title,seriesName:Series Name,seriesId:Series Id,mlHtmlFlag:ML Html flag,promoDates:Promo Dates,promoStartDate:Promo Start Date,promoEndDate:Promo End Date,issueCompleteFlag:Issue Complete Flag,scope:Scope,purpose:Purpose,standardFamilyTitle:Standard Family Title,thumbnailImg:Thumbnail Img,supplementFile:Supplement File,courseFile:Course File,supplement:Supplement,courseAuthor:Course Author,pdhs:Pdhs,ceus:Ceus,courseFirstFrame:FirstFrame Img,idSubTopic:Id Sub Topic,certificateUrl:Certificate Url,standardRoot:Standard Root,icsTerms:Standards ICS Terms,impactStatement:Impact Statement,plagiarizedFlag:Plagiarized Flag,affirmedDate:Affirmed Date,sourcePdf:Source Pdf,orcid:Author ORCID,algorithmFlag:Algorithm Flag,fundingAgency:Funding Agency,funder:Funder,pricingKey:Map Pricing Key,publicationRollup:Rollup Key,collection:Collection,previewImage:Preview Image,regularDate:Regular Date,ContentType:Content Type,ringgoldIds:Ringgold ID,figure:Figure,mediaPath:Media Path,publicationVolumeOnly:Publication Volume Only,Search_All:All Metadata,Search_All_Text:Full Text & Metadata,fullText:Full Text Only,TypeAheadTerms:Type Ahead Terms,ContentType:Content Type,Author:Author,Affiliation:Affiliation,Topic:Topic,PublicationTitle:Publication Title,PublicationYear:Year,Publisher:Publisher,ConferenceCountry:Conference Country,ConferenceLocation:Conference Location,StandardStatus:Standard Status,ConferenceYear:Conference Year,PublicationPackage:Subscribed Content,StandardPackage:Standard Package,ReadingRoom:Reading Room,StandardTitle:Standard Title,StdDictionaryTerms:Standards Dictionary Terms,TitleRange:Publication Range,StandardRange:Standard Range,RecordType:Record Type,MediaType:Media Type,BookType:Book Type,CourseType:Course Type,PublicationStandardRange:Publication Standard Range,PerpetualYear:Perpetual Year,OpacTitleRange:Opac Title Range,BookSeries:Book Series,SubjectCategory:Subject Category,Sessions:Sessions,TypeAheadPublication:Type Ahead Publication,SubTopic:Sub Topic,CourseDuration:Course Duration,CourseLevel:Course Level,StandardType:Standard Type,StandardSubtype:Standard SubType,StandardModifier:Standard Modifier,IcsTerms1:Ics Terms 1,IcsTerms2:Ics Terms 2,IcsTerms3:Ics Terms 3,SupplementalItem:Supplemental Items,CourseDuration:Course Duration,SpecialSection:Topics,SocietySection:Society Sections,PublicationTopics:Publication Topics';
	var SEARCH_FIELD_REFERENCES = new Array();
	var SEARCH_FIELD_DISPLAYS = new Array();
	var searchFields = ALL_SEARCH_FIELDS.split(",");
	for (var j = 0; j < searchFields.length; j++) {
		parts = searchFields[j].split(":");
		SEARCH_FIELD_REFERENCES[j] = parts[0];
		SEARCH_FIELD_DISPLAYS[j] = parts[1];
	}
	

	var refSite='https://ieeexplore.ieee.org';
	var refSiteName="IEEE Xplore";
	var applicationName = 'Xplore';
	var MC_OPERATION_DELAY_TIMEOUT='5000';
	var MC_ADDING_DELAY_MSG='Please wait.The selected item(s) is being added to the cart.';
	var MC_TIMEOUT='60000';
	var MC_OPERATION_DELAY_MSG_FLAG='true';

	var MEMBER_PROFILE_CHANGE_USERNAMEPASS_LINK = 'https://www.ieee.org/profile/changeusrpwd/showChangeUsrPwdPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_MY_PROFILE ='https://www.ieee.org/profile/myprofile/myprofile.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_PROFILE_ADDRESSINFO_LINK = 'https://www.ieee.org/profile/address/getAddrInfoPage.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_PROFILE_PAYMENTINFO_LINK = 'https://www.ieee.org/profile/payment/showPaymentHome.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_PROFILE_ORDER_HISTORY_LINK = 'https://www.ieee.org/profile/vieworder/showOrderHistory.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_USER_COMMUNICATION_LINK = 'https://www.ieee.org/ieee-privacyportal/app/ibp?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_EDUCATIONAL_PROFILE_LINK = 'https://www.ieee.org/profile/profedu/getProfEduInformation.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var MEMBER_TECHNICAL_INTERESTS_LINK = 'https://www.ieee.org/profile/tips/getTipsInfo.html?refSite=https://ieeexplore.ieee.org&refSiteName=IEEE Xplore';
	var HELPFILE_RELATIVE_PATH = '/Xplorehelp';
	
	//content types
	var CONTENT_TYPE_PARAM = 'contentType';
	var CONTENT_TYPE_BOOKS = 'Books';
	var CONTENT_TYPE_COURSES = 'Courses';
	var CONTENT_TYPE_STANDARDS = 'Standards';
	var CONTENT_TYPE_CONFERENCES = 'Conferences';
	var CONTENT_TYPE_JOURNALS = 'Journals';
	var CONTENT_TYPE_EARLY_ACCESS = 'Early Access Articles';
	
	//User Preferences
	var citFormat = "";
	var dlFormat = "";
	var myProjectLimit = 15;
	var myProjectDocumentLimit = 1000;
	var myProjectDocumentTagLimit = 50;
	
	
	//Google ReCaptcha public Key 
	var RECAPTCHA_PUBLIC_KEY = '6Ld6GEUUAAAAALdaAmeGUhZyz1KFFHnd5oCaTW-t';

	var seamlessAccessPersistenceUrl = 'https://service.seamlessaccess.org/ps/';
</script>

					
					
								
			
				
					
					
								
			
				
					
					
								<script type="text/javascript" src='/assets/dist/js/history.js?cv=20240305_000000' charset="utf-8"></script>
					
					
								<script type="text/javascript" src='/assets/dist/js/cart/cartScroll.js?cv=20240305_000000' charset="utf-8"></script>
					
					
								<script type="text/javascript" src='/assets/dist/js/cart/minicart.js?cv=20240305_000000' charset="utf-8"></script>
					
					
								<script type="text/javascript" src='/assets/dist/js/master.js?cv=20240305_000000' charset="utf-8"></script>
					
								
<script>

j$('document').ready(function(){
	if (Cookies.get('legacyUserName')) {
		if (IBP_WS_ENABLED_FLAG){
			Modal.refreshLegacyAccountTransition('/xpl/mwLegacyAccountTransition.jsp');
		}
	}
});

</script>

</g:compress>

<script>
	// Get/Set XPL namespace.
	window.xpl = window.xpl || {};
	
	// Set constants/application properties.
	xpl.properties = { 
			collabratec: { 
					url: 'https://ieee-collabratec.ieee.org/app/library'
			}
	};
	
	xpl.properties.details = {
			oqs: ''
	};
</script>
					
			
	<!--Begin Optional Configuration-->
	<script type="text/javascript" src='https://www.ieee.org/ieee-mashup/js/common/jquery.json-2.2.min.js'></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/common/postmessage-min.js" ></script>
	<script type="text/javascript" src='https://www.ieee.org/ieee-mashup/js/common/jquery.cookie-min.js'></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/auth/ieee-auth-constants-min.js"></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/auth/ieee-auth-include-min.js" ></script>
	<script type="text/javascript" src='https://www.ieee.org/ieee-mashup/js/minicart/ieee-mini-cart-constants-min.js'></script>


	<script type="text/javascript" src='https://www.ieee.org/ieee-mashup/js/minicart/ieee-mashup-util-min.js'></script>
	<script type="text/javascript" src="https://www.ieee.org/ieee-mashup/js/common/jquery.ba-jqmq-min.js"></script>
	<script type="text/javaScript" src="https://www.ieee.org/ieee-mashup/js/minicart/ieee-minicart-include-min.js"> </script>

	<!--End Optional Configuration-->


<!-- Removed due to network issues when loading in China -->
<!-- <script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#pubid=ra-5005a435228f9245" async="async"></script>-->

<!-- Load Mathjax and process the document for Mathjax characters -->


<!-- <script type="text/javascript" src="/xploreAssets/MathJax-274/MathJax.js?config=default"></script> -->


<script defer>
	MathJax.Hub.Queue(["Typeset", MathJax.Hub, document.body]);
</script>


<script>
	window.PARSELY = window.PARSELY || {
	    use_localstorage: true
	};
</script>
<script id="parsely-cfg" src="//cdn.parsely.com/keys/ieeexplore.ieee.org/p.js"></script>


					</div>
				</div>

			
				<script>
					// set $ alias back to jQuery because noConflict mode is used in legacy pages
					window.$ = jQuery;
				</script>
			
		</div><!-- /#LayoutWrapper -->
	</body>
</html>
"""
