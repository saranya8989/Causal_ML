import sys
import func
import glob,os
from scipy.ndimage import gaussian_filter1d
from tqdm import tqdm
import numpy as np
from copy import deepcopy
from natsort import natsorted

script_name = sys.argv[0]
tau_min = int(sys.argv[1])    
tau_max = int(sys.argv[2])
pc_alphaa = float(sys.argv[3])
alpha_level = float(sys.argv[4])
seednum = int(sys.argv[5])

print(f"Script {script_name} was run with tmax: {tau_min}, tmin: {tau_max}, pc_alpha: {pc_alphaa}, alpha_level: {alpha_level}, seed: {seednum}")

#tigramite path in the env:/work/FAC/FGSE/IDYST/tbeucler/default/saranya/miniconda3/envs/unil_tigramite/lib/python3.8/site-packages/tigramite/
p1="/work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/timeseries_csv/ts_wp/"
#p2="../../targets/"

tcwp2=func._process_dataset(glob.glob(p1+'*2020chanhom*')[0]).values
tcwp3=func._process_dataset(glob.glob(p1+'*2020saudel*')[0]).values
tcwp4=func._process_dataset(glob.glob(p1+'*2020molave*')[0]).values
tcwp5=func._process_dataset(glob.glob(p1+'*2020goni*')[0]).values
tcwp6=func._process_dataset(glob.glob(p1+'*2020atsani*')[0]).values
tcwp7=func._process_dataset(glob.glob(p1+'*2020vamco*')[0]).values
tcwp8=func._process_dataset(glob.glob(p1+'*2019neoguri*')[0]).values
tcwp9=func._process_dataset(glob.glob(p1+'*2019bualoi*')[0]).values
tcwp10=func._process_dataset(glob.glob(p1+'*2019halong*')[0]).values
tcwp11=func._process_dataset(glob.glob(p1+'*2019nakri*')[0]).values
tcwp12=func._process_dataset(glob.glob(p1+'*2019fengshen*')[0]).values
tcwp13=func._process_dataset(glob.glob(p1+'*2019kalmaegi*')[0]).values
tcwp14=func._process_dataset(glob.glob(p1+'*2019fungwong*')[0]).values
tcwp15=func._process_dataset(glob.glob(p1+'*2019kammuri*')[0]).values
tcwp16=func._process_dataset(glob.glob(p1+'*2018jelawat*')[0]).values
tcwp17=func._process_dataset(glob.glob(p1+'*2018maliksi*')[0]).values
tcwp18=func._process_dataset(glob.glob(p1+'*2018kongrey*')[0]).values
tcwp19=func._process_dataset(glob.glob(p1+'*2018yutu*')[0]).values
#tcwp20=func._process_dataset(glob.glob(p1+'*2017muifa*')[0]).values
tcwp21=func._process_dataset(glob.glob(p1+'*2017lan*')[0]).values
tcwp22=func._process_dataset(glob.glob(p1+'*2017haikul*')[0]).values
tcwp23=func._process_dataset(glob.glob(p1+'*2016megi*')[0]).values
tcwp24=func._process_dataset(glob.glob(p1+'*2016sarika*')[0]).values
tcwp25=func._process_dataset(glob.glob(p1+'*2016haima*')[0]).values
tcwp26=func._process_dataset(glob.glob(p1+'*2015maysak*')[0]).values
tcwp27=func._process_dataset(glob.glob(p1+'*2015koppu*')[0]).values
tcwp28=func._process_dataset(glob.glob(p1+'*2015infa*')[0]).values
tcwp29=func._process_dataset(glob.glob(p1+'*2014tapah*')[0]).values
tcwp30=func._process_dataset(glob.glob(p1+'*2014nuri*')[0]).values
tcwp31=func._process_dataset(glob.glob(p1+'*2014hagupit*')[0]).values
tcwp32=func._process_dataset(glob.glob(p1+'*2013yagi*')[0]).values
tcwp33=func._process_dataset(glob.glob(p1+'*2013fitow*')[0]).values
tcwp34=func._process_dataset(glob.glob(p1+'*2013danas*')[0]).values
tcwp35=func._process_dataset(glob.glob(p1+'*2013francisco*')[0]).values
tcwp36=func._process_dataset(glob.glob(p1+'*2013krosa*')[0]).values
tcwp37=func._process_dataset(glob.glob(p1+'*2013haiyan*')[0]).values
tcwp38=func._process_dataset(glob.glob(p1+'*2012guchol*')[0]).values
tcwp39=func._process_dataset(glob.glob(p1+'*2012gaemi*')[0]).values
tcwp40=func._process_dataset(glob.glob(p1+'*2012maria*')[0]).values
tcwp41=func._process_dataset(glob.glob(p1+'*2012sontinh*')[0]).values
tcwp42=func._process_dataset(glob.glob(p1+'*2012bopha*')[0]).values
tcwp43=func._process_dataset(glob.glob(p1+'*2011songda*')[0]).values
tcwp44=func._process_dataset(glob.glob(p1+'*2011haima*')[0]).values
tcwp45=func._process_dataset(glob.glob(p1+'*2011nalgae*')[0]).values
tcwp46=func._process_dataset(glob.glob(p1+'*2011washi*')[0]).values
tcwp47=func._process_dataset(glob.glob(p1+'*2010OMAIS*')[0]).values
tcwp48=func._process_dataset(glob.glob(p1+'*2010CONSON*')[0]).values
tcwp49=func._process_dataset(glob.glob(p1+'*2010CHANTHU*')[0]).values
tcwp50=func._process_dataset(glob.glob(p1+'*2010DIANMU*')[0]).values
tcwp51=func._process_dataset(glob.glob(p1+'*2010LIONROCK*')[0]).values
tcwp52=func._process_dataset(glob.glob(p1+'*2010MALOU*')[0]).values
tcwp53=func._process_dataset(glob.glob(p1+'*2010FANAPI*')[0]).values
tcwp54=func._process_dataset(glob.glob(p1+'*2010MALAKAS*')[0]).values
tcwp55=func._process_dataset(glob.glob(p1+'*2010MEGI*')[0]).values
tcwp56=func._process_dataset(glob.glob(p1+'*2010CHABA*')[0]).values
tcwp57=func._process_dataset(glob.glob(p1+'*2010OMEKA*')[0]).values
tcwp58=func._process_dataset(glob.glob(p1+'*2009KUJIRA*')[0]).values
tcwp59=func._process_dataset(glob.glob(p1+'*2009CHAN-HOM*')[0]).values
tcwp60=func._process_dataset(glob.glob(p1+'*2009LINFA*')[0]).values
tcwp61=func._process_dataset(glob.glob(p1+'*2009MORAKOT*')[0]).values
tcwp62=func._process_dataset(glob.glob(p1+'*2009ETAU*')[0]).values
tcwp63=func._process_dataset(glob.glob(p1+'*2009VAMCO*')[0]).values
tcwp64=func._process_dataset(glob.glob(p1+'*2009KROVANH*')[0]).values
tcwp65=func._process_dataset(glob.glob(p1+'*2009DUJUAN*')[0]).values
tcwp66=func._process_dataset(glob.glob(p1+'*2009CHOI-WAN*')[0]).values
tcwp67=func._process_dataset(glob.glob(p1+'*2009PARMA*')[0]).values
tcwp68=func._process_dataset(glob.glob(p1+'*2009MELOR*')[0]).values
tcwp69=func._process_dataset(glob.glob(p1+'*2009LUPIT*')[0]).values
tcwp70=func._process_dataset(glob.glob(p1+'*2009MIRINAE*')[0]).values
tcwp71=func._process_dataset(glob.glob(p1+'*2009NIDA*')[0]).values
tcwp72=func._process_dataset(glob.glob(p1+'*2008NEOGURI*')[0]).values
tcwp73=func._process_dataset(glob.glob(p1+'*2008RAMMASUN*')[0]).values
tcwp74=func._process_dataset(glob.glob(p1+'*2008NAKRI*')[0]).values
tcwp75=func._process_dataset(glob.glob(p1+'*2008FENGSHEN*')[0]).values
tcwp76=func._process_dataset(glob.glob(p1+'*2008KALMAEGI*')[0]).values
tcwp77=func._process_dataset(glob.glob(p1+'*2008FUNG-WONG*')[0]).values
tcwp78=func._process_dataset(glob.glob(p1+'*2008VONGFONG*')[0]).values
tcwp79=func._process_dataset(glob.glob(p1+'*2008NURI*')[0]).values
tcwp80=func._process_dataset(glob.glob(p1+'*2008SINLAKU*')[0]).values
tcwp81=func._process_dataset(glob.glob(p1+'*2008HAGUPIT*')[0]).values
tcwp82=func._process_dataset(glob.glob(p1+'*2008JANGMI*')[0]).values
tcwp83=func._process_dataset(glob.glob(p1+'*2008HIGOS*')[0]).values
tcwp84=func._process_dataset(glob.glob(p1+'*2008MAYSAK*')[0]).values
tcwp85=func._process_dataset(glob.glob(p1+'*2008DOLPHIN*')[0]).values
tcwp86=func._process_dataset(glob.glob(p1+'*2007KONG-REY*')[0]).values
tcwp87=func._process_dataset(glob.glob(p1+'*2007MAN-YI*')[0]).values
tcwp88=func._process_dataset(glob.glob(p1+'*2007USAGI*')[0]).values
tcwp89=func._process_dataset(glob.glob(p1+'*2007PABUK*')[0]).values
tcwp90=func._process_dataset(glob.glob(p1+'*2007SEPAT*')[0]).values
tcwp91=func._process_dataset(glob.glob(p1+'*2007FITOW*')[0]).values
tcwp92=func._process_dataset(glob.glob(p1+'*2007DANAS*')[0]).values
tcwp93=func._process_dataset(glob.glob(p1+'*2007NARI*')[0]).values
tcwp94=func._process_dataset(glob.glob(p1+'*2007WIPHA*')[0]).values
tcwp95=func._process_dataset(glob.glob(p1+'*2007LEKIMA*')[0]).values
tcwp96=func._process_dataset(glob.glob(p1+'*2007KROSA*')[0]).values
tcwp97=func._process_dataset(glob.glob(p1+'*2007LINGLING*')[0]).values
tcwp98=func._process_dataset(glob.glob(p1+'*2007PEIPAH*')[0]).values
tcwp99=func._process_dataset(glob.glob(p1+'*2007HAGIBIS*')[0]).values
tcwp100=func._process_dataset(glob.glob(p1+'*2007MITAG*')[0]).values
tcwp101=func._process_dataset(glob.glob(p1+'*2006CHANCHU*')[0]).values
tcwp102=func._process_dataset(glob.glob(p1+'*2006EWINIAR*')[0]).values
tcwp103=func._process_dataset(glob.glob(p1+'*2006BILIS*')[0]).values
tcwp104=func._process_dataset(glob.glob(p1+'*2006KAEMI*')[0]).values
tcwp105=func._process_dataset(glob.glob(p1+'*2006PRAPIROON*')[0]).values
tcwp106=func._process_dataset(glob.glob(p1+'*2006SAOMAI*')[0]).values
tcwp107=func._process_dataset(glob.glob(p1+'*2006WUKONG*')[0]).values
tcwp108=func._process_dataset(glob.glob(p1+'*2006IOKE*')[0]).values
tcwp109=func._process_dataset(glob.glob(p1+'*2006SHANSHAN*')[0]).values
tcwp110=func._process_dataset(glob.glob(p1+'*2006MUKDA*')[0]).values
tcwp111=func._process_dataset(glob.glob(p1+'*2006XANGSANE*')[0]).values
tcwp112=func._process_dataset(glob.glob(p1+'*2006BEBINCA*')[0]).values
tcwp113=func._process_dataset(glob.glob(p1+'*2006SOULIK*')[0]).values
tcwp114=func._process_dataset(glob.glob(p1+'*2006CIMARON*')[0]).values
tcwp115=func._process_dataset(glob.glob(p1+'*2006CHEBI*')[0]).values
tcwp116=func._process_dataset(glob.glob(p1+'*2006DURIAN*')[0]).values
tcwp117=func._process_dataset(glob.glob(p1+'*2006UTOR*')[0]).values
tcwp118=func._process_dataset(glob.glob(p1+'*2005KULAP*')[0]).values
tcwp119=func._process_dataset(glob.glob(p1+'*2005ROKE*')[0]).values
tcwp120=func._process_dataset(glob.glob(p1+'*2005SONCA*')[0]).values
tcwp121=func._process_dataset(glob.glob(p1+'*2005HAITANG*')[0]).values
tcwp122=func._process_dataset(glob.glob(p1+'*2005NALGAE*')[0]).values
tcwp123=func._process_dataset(glob.glob(p1+'*2005BANYAN*')[0]).values
tcwp124=func._process_dataset(glob.glob(p1+'*2005MATSA*')[0]).values
tcwp125=func._process_dataset(glob.glob(p1+'*2005GUCHOL*')[0]).values
tcwp126=func._process_dataset(glob.glob(p1+'*2005MAWAR*')[0]).values
tcwp127=func._process_dataset(glob.glob(p1+'*2005TALIM*')[0]).values
tcwp128=func._process_dataset(glob.glob(p1+'*2005NABI*')[0]).values
tcwp129=func._process_dataset(glob.glob(p1+'*2005KHANUN*')[0]).values
tcwp130=func._process_dataset(glob.glob(p1+'*2005DAMREY*')[0]).values
tcwp131=func._process_dataset(glob.glob(p1+'*2005SAOLA*')[0]).values
tcwp132=func._process_dataset(glob.glob(p1+'*2005LONGWANG*')[0]).values
tcwp133=func._process_dataset(glob.glob(p1+'*2005KIROGI*')[0]).values
tcwp134=func._process_dataset(glob.glob(p1+'*2005TEMBIN*')[0]).values
tcwp135=func._process_dataset(glob.glob(p1+'*2005BOLAVEN*')[0]).values
tcwp136=func._process_dataset(glob.glob(p1+'*2004SUDAL*')[0]).values
tcwp137=func._process_dataset(glob.glob(p1+'*2004NIDA*')[0]).values
tcwp138=func._process_dataset(glob.glob(p1+'*2004CHANTHU*')[0]).values
tcwp139=func._process_dataset(glob.glob(p1+'*2004DIANMU*')[0]).values
tcwp140=func._process_dataset(glob.glob(p1+'*2004MINDULLE*')[0]).values
tcwp141=func._process_dataset(glob.glob(p1+'*2004TINGTING*')[0]).values
tcwp142=func._process_dataset(glob.glob(p1+'*2004NAMTHEUN*')[0]).values
tcwp143=func._process_dataset(glob.glob(p1+'*2004MERANTI*')[0]).values
tcwp144=func._process_dataset(glob.glob(p1+'*2004RANANIM*')[0]).values
tcwp145=func._process_dataset(glob.glob(p1+'*2004MEGI*')[0]).values
tcwp146=func._process_dataset(glob.glob(p1+'*2004CHABA*')[0]).values
tcwp147=func._process_dataset(glob.glob(p1+'*2004AERE*')[0]).values
tcwp148=func._process_dataset(glob.glob(p1+'*2004SONGDA*')[0]).values
tcwp149=func._process_dataset(glob.glob(p1+'*2004MEARI*')[0]).values
tcwp150=func._process_dataset(glob.glob(p1+'*2004MA-ON*')[0]).values
tcwp151=func._process_dataset(glob.glob(p1+'*2004TOKAGE*')[0]).values
tcwp152=func._process_dataset(glob.glob(p1+'*2004NOCK-TEN*')[0]).values
tcwp153=func._process_dataset(glob.glob(p1+'*2004MUIFA*')[0]).values
tcwp154=func._process_dataset(glob.glob(p1+'*2004NANMADOL*')[0]).values
tcwp155=func._process_dataset(glob.glob(p1+'*2004NORU*')[0]).values
tcwp156=func._process_dataset(glob.glob(p1+'*2003SOUDELOR*')[0]).values
tcwp157=func._process_dataset(glob.glob(p1+'*2003KUJIRA*')[0]).values
tcwp158=func._process_dataset(glob.glob(p1+'*2003CHAN-HOM*')[0]).values
tcwp159=func._process_dataset(glob.glob(p1+'*2003IMBUDO*')[0]).values
tcwp160=func._process_dataset(glob.glob(p1+'*2003NANGKA*')[0]).values
tcwp161=func._process_dataset(glob.glob(p1+'*2003KONI*')[0]).values
tcwp162=func._process_dataset(glob.glob(p1+'*2003ETAU*')[0]).values
tcwp163=func._process_dataset(glob.glob(p1+'*2003KROVANH*')[0]).values
tcwp164=func._process_dataset(glob.glob(p1+'*2003DUJUAN*')[0]).values
tcwp165=func._process_dataset(glob.glob(p1+'*2003MAEMI*')[0]).values
tcwp166=func._process_dataset(glob.glob(p1+'*2003CHOI-WAN*')[0]).values
tcwp167=func._process_dataset(glob.glob(p1+'*2003KOPPU*')[0]).values
tcwp168=func._process_dataset(glob.glob(p1+'*2003KETSANA*')[0]).values
tcwp169=func._process_dataset(glob.glob(p1+'*2003MELOR*')[0]).values
tcwp170=func._process_dataset(glob.glob(p1+'*2003NEPARTAK*')[0]).values
tcwp171=func._process_dataset(glob.glob(p1+'*2003LUPIT*')[0]).values
tcwp172=func._process_dataset(glob.glob(p1+'*2002MITAG*')[0]).values
tcwp173=func._process_dataset(glob.glob(p1+'*2002HAGIBIS*')[0]).values
tcwp174=func._process_dataset(glob.glob(p1+'*2002CHATAAN*')[0]).values
tcwp175=func._process_dataset(glob.glob(p1+'*2002RAMMASUN*')[0]).values
tcwp176=func._process_dataset(glob.glob(p1+'*2002HALONG*')[0]).values
tcwp177=func._process_dataset(glob.glob(p1+'*2002FENGSHEN*')[0]).values
tcwp178=func._process_dataset(glob.glob(p1+'*2002FUNG-WONG*')[0]).values
tcwp179=func._process_dataset(glob.glob(p1+'*2002PHANFONE*')[0]).values
tcwp180=func._process_dataset(glob.glob(p1+'*2002RUSA*')[0]).values
tcwp181=func._process_dataset(glob.glob(p1+'*2002ELE*')[0]).values
tcwp182=func._process_dataset(glob.glob(p1+'*2002SINLAKU*')[0]).values
tcwp183=func._process_dataset(glob.glob(p1+'*2002HAGUPIT*')[0]).values
tcwp184=func._process_dataset(glob.glob(p1+'*2002MEKKHALA*')[0]).values
tcwp185=func._process_dataset(glob.glob(p1+'*2002HIGOS*')[0]).values
tcwp186=func._process_dataset(glob.glob(p1+'*2002BAVI*')[0]).values
tcwp187=func._process_dataset(glob.glob(p1+'*2002HUKO*')[0]).values
tcwp188=func._process_dataset(glob.glob(p1+'*2002HAISHEN*')[0]).values
tcwp189=func._process_dataset(glob.glob(p1+'*2002PONGSONA*')[0]).values
tcwp190=func._process_dataset(glob.glob(p1+'*2001CIMARON*')[0]).values
tcwp191=func._process_dataset(glob.glob(p1+'*2001CHEBI*')[0]).values
tcwp192=func._process_dataset(glob.glob(p1+'*2001UTOR*')[0]).values
tcwp193=func._process_dataset(glob.glob(p1+'*2001KONG-REY*')[0]).values
tcwp194=func._process_dataset(glob.glob(p1+'*2001FRANCISCO*')[0]).values
tcwp195=func._process_dataset(glob.glob(p1+'*2001MAN-YI*')[0]).values
tcwp196=func._process_dataset(glob.glob(p1+'*2001PABUK*')[0]).values
tcwp197=func._process_dataset(glob.glob(p1+'*2001WUTIP*')[0]).values
tcwp198=func._process_dataset(glob.glob(p1+'*2001FITOW*')[0]).values
tcwp199=func._process_dataset(glob.glob(p1+'*2001NARI*')[0]).values
tcwp200=func._process_dataset(glob.glob(p1+'*2001VIPA*')[0]).values
tcwp201=func._process_dataset(glob.glob(p1+'*2001FRANCISCO*')[0]).values
tcwp202=func._process_dataset(glob.glob(p1+'*2001LEKIMA*')[0]).values
tcwp203=func._process_dataset(glob.glob(p1+'*2001KROSA*')[0]).values
tcwp204=func._process_dataset(glob.glob(p1+'*2001HAIYAN*')[0]).values
tcwp205=func._process_dataset(glob.glob(p1+'*2001PODUL*')[0]).values
tcwp206=func._process_dataset(glob.glob(p1+'*2001LINGLING*')[0]).values
tcwp207=func._process_dataset(glob.glob(p1+'*2001FAXAI*')[0]).values


ddwp={'cyclone2':tcwp2,'cyclone3':tcwp3,'cyclone4':tcwp4,'cyclone5':tcwp5,'cyclone6':tcwp6,
      'cyclone7':tcwp7, 'cyclone8':tcwp8,'cyclone9':tcwp9,'cyclone10':tcwp10,'cyclone11':tcwp11,'cyclone12':tcwp12,
      'cyclone13':tcwp13,'cyclone14':tcwp14,'cyclone15':tcwp15,'cyclone16':tcwp16,'cyclone17':tcwp17,
      'cyclone18':tcwp18,'cyclone19':tcwp19,'cyclone21':tcwp21,'cyclone22':tcwp22,'cyclone23':tcwp23,'cyclone24':tcwp24,
      'cyclone25':tcwp25,'cyclone26':tcwp26,'cyclone27':tcwp27,'cyclone28':tcwp28,'cyclone29':tcwp29,'cyclone30':tcwp30,
      'cyclone31':tcwp31,'cyclone32':tcwp32,'cyclone33':tcwp33,'cyclone34':tcwp34,'cyclone35':tcwp35,'cyclone36':tcwp36,
      'cyclone37':tcwp37,'cyclone38':tcwp38,'cyclone39':tcwp39,'cyclone40':tcwp40,'cyclone41':tcwp41,'cyclone42':tcwp42,
      'cyclone43':tcwp43,'cyclone44':tcwp44,'cyclone45':tcwp45,'cyclone46':tcwp46,'cyclone47':tcwp47,'cyclone48':tcwp48,
      'cyclone49':tcwp49,'cyclone50':tcwp50,'cyclone51':tcwp51,
      'cyclone52':tcwp52, 'cyclone53':tcwp53,'cyclone54':tcwp54,'cyclone55':tcwp55,'cyclone56':tcwp56,'cyclone57':tcwp57,
      'cyclone58':tcwp58,'cyclone59':tcwp59,'cyclone60':tcwp60,'cyclone61':tcwp61,'cyclone62':tcwp62,'cyclone63':tcwp63,
      'cyclone64':tcwp64,'cyclone65':tcwp65,'cyclone66':tcwp66,'cyclone67':tcwp67,'cyclone68':tcwp68,'cyclone69':tcwp69,
      'cyclone70':tcwp70,'cyclone71':tcwp71,'cyclone72':tcwp72,'cyclone73':tcwp73,'cyclone74':tcwp74,'cyclone75':tcwp75,
      'cyclone76':tcwp76,'cyclone77':tcwp77,'cyclone78':tcwp78,'cyclone79':tcwp79,'cyclone80':tcwp80,'cyclone81':tcwp81,
      'cyclone82':tcwp82,'cyclone83':tcwp83,'cyclone84':tcwp84,'cyclone85':tcwp85,'cyclone86':tcwp86,'cyclone87':tcwp87,
      'cyclone88':tcwp88,'cyclone89':tcwp89,'cyclone90':tcwp90,'cyclone91':tcwp91,'cyclone92':tcwp92,'cyclone93':tcwp93,
      'cyclone94':tcwp94,'cyclone95':tcwp95,'cyclone96':tcwp96,'cyclone97':tcwp97,'cyclone98':tcwp98,'cyclone99':tcwp99,
      'cyclone100':tcwp100,'cyclone101':tcwp101,'cyclone102':tcwp102,'cyclone103':tcwp103,'cyclone104':tcwp104,
      'cyclone105':tcwp105,'cyclone106':tcwp106,'cyclone107':tcwp107,'cyclone108':tcwp108,'cyclone109':tcwp109,
      'cyclone110':tcwp110,'cyclone111':tcwp111,'cyclone112':tcwp112,'cyclone113':tcwp113,'cyclone114':tcwp114,
      'cyclone115':tcwp115,'cyclone116':tcwp116,'cyclone117':tcwp117,'cyclone118':tcwp118,'cyclone119':tcwp119,
      'cyclone120':tcwp120,'cyclone121':tcwp121,'cyclone122':tcwp122,'cyclone123':tcwp123,'cyclone124':tcwp124,
      'cyclone125':tcwp125,'cyclone126':tcwp126,'cyclone127':tcwp127,'cyclone128':tcwp128,'cyclone129':tcwp129,
      'cyclone130':tcwp130,'cyclone131':tcwp131,'cyclone132':tcwp132,'cyclone133':tcwp133,'cyclone134':tcwp134,
      'cyclone135':tcwp135,'cyclone136':tcwp136,'cyclone137':tcwp137,'cyclone138':tcwp138,'cyclone139':tcwp139,
      'cyclone140':tcwp140,'cyclone141':tcwp141,'cyclone142':tcwp142,'cyclone143':tcwp143,'cyclone144':tcwp144,
      'cyclone145':tcwp145,'cyclone146':tcwp146,'cylone147':tcwp147,'cyclone148':tcwp148,'cyclone149':tcwp149,'cyclone150':tcwp150,
      'cyclone151':tcwp151,'cyclone152':tcwp152,'cyclone153':tcwp153,'cyclone154':tcwp154,'cyclone155':tcwp155,
      'cyclone156':tcwp156,'cyclone157':tcwp157,'cyclone158':tcwp158,'cyclone159':tcwp159,'cyclone160':tcwp160,
      'cyclone161':tcwp161,'cyclone162':tcwp162,'cyclone163':tcwp163,'cyclone164':tcwp164,'cyclone165':tcwp165,
      'cyclone166':tcwp166,'cyclone167':tcwp167,'cyclone168':tcwp168,'cyclone169':tcwp169,'cyclone170':tcwp170,
      'cyclone171':tcwp171,'cyclone172':tcwp172,'cyclone173':tcwp173,'cyclone174':tcwp174,'cyclone175':tcwp175,
      'cyclone176':tcwp176,'cyclone177':tcwp177,'cyclone178':tcwp178,'cyclone179':tcwp179,'cyclone180':tcwp180,
      'cyclone181':tcwp181,'cyclone182':tcwp182,'cyclone183':tcwp183,'cyclone184':tcwp184,'cyclone185':tcwp185,
      'cyclone186':tcwp186,'cyclone187':tcwp187,'cyclone188':tcwp188,'cyclone189':tcwp189,'cyclone190':tcwp190,
      'cyclone191':tcwp191,'cyclone192':tcwp192,'cyclone193':tcwp193,'cyclone194':tcwp194,'cyclone195':tcwp195,
      'cyclone196':tcwp196,'cylone197':tcwp197,'cyclone198':tcwp198,'cyclone199':tcwp199,'cyclone200':tcwp200,
      'cyclone201':tcwp201,'cyclone202':tcwp202,'cyclone203':tcwp203,'cyclone204':tcwp204,'cyclone205':tcwp205,
      'cyclone206':tcwp206,'cyclone207':tcwp207}

testcyclone_dict = {}
newtestfilelist_f = natsorted(glob.glob('/work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/timeseries_csv/new_storms_wpac/*'))[-62:-7]
for ind,obj in tqdm(enumerate(newtestfilelist_f)):
    testcyclone_dict['testcyclone'+str(ind)] = func._process_dataset(obj).values
    
newddwp = {}
for inte,item in enumerate(ddwp.keys()):
    newddwp[inte] = ddwp[item]
indices = {}
for ind,varnames in enumerate(newddwp.keys()):
    indices[varnames] = np.argmin(gaussian_filter1d(newddwp[varnames][:,1],3))

newddwp_test = {}
for inte,item in enumerate(testcyclone_dict.keys()):
    newddwp_test[inte] = testcyclone_dict[item]
indices_test = {}
for ind,varnames in enumerate(newddwp_test.keys()):
    indices_test[varnames] = np.argmin(gaussian_filter1d(newddwp_test[varnames][:,1],3))

def align_data(refpoint=None,individualpoint=None,data=None):
    newtraincyclone2 = np.zeros((data.shape[0]+(refpoint-individualpoint),data.shape[1]))
    for i in range((data.shape[1])):
        newtraincyclone2[:,i] = np.concatenate([np.ones((refpoint-individualpoint))*(-999.),data[:,i]])
    return newtraincyclone2

splitsize=55
pc_type = 'run_pcstable'
var_names=func._process_dataset(glob.glob(p1+'*2020chanhom*')[0]).columns.values.tolist()

aligned_newddwp = {}
for intt,obj in enumerate(newddwp.keys()):
    aligned_newddwp[obj] = align_data(np.asarray(list(indices.values())).max(),indices[obj],newddwp[obj])

aligned_newddwp_test = {}
for intt,obj in enumerate(newddwp_test.keys()):
    aligned_newddwp_test[obj] = align_data(np.asarray(list(indices_test.values())).max(),indices_test[obj],newddwp_test[obj])
    
for pc_alpha in ([pc_alphaa]):#np.linspace(0.9,0.99,10)):#,0.1,0.05,0.01,1e-3,1e-4,1e-5,1e-6,1e-7,1e-8]):_
    testindex = (func.Pipeline(aligned_newddwp,pc_alpha,alpha_level,pc_type=pc_type,tau_min0=tau_min,tau_max0=tau_max,\
                          target=None,var_name=var_names,seed=seednum).random_testindex(205,splitsize))
    traindata,validdata,testdata = func.Pipeline(aligned_newddwp,pc_alpha,alpha_level,pc_type=pc_type,tau_min0=tau_min,tau_max0=tau_max,\
                                            target=None,var_name=var_names,seed=seednum).splitdata(testindex)
    newtestdata = deepcopy(aligned_newddwp_test)
    result,val_min,pval_max = func.Pipeline(traindata,pc_alpha,alpha_level,pc_type=pc_type,tau_min0=tau_min,tau_max0=tau_max,\
                      target=None,var_name=var_names,seed=seednum).run_tigramite(int(205-splitsize))
    saveresults = {'result':result,'val_min':val_min,'pval_max':pval_max}
    var_and_lag = [result[0],result[1],result[2]]
    
    validdata=func.do_num_to_nan(validdata)
    testdata=func.do_num_to_nan(testdata)
    newtestdata=func.do_num_to_nan(newtestdata)
    
    wpac_mlr_precip,X_precip,y_precip = func.trainMLR_target(traindata=traindata,validdata=validdata,testdata=testdata,newtestdata=newtestdata,pc_alpha=pc_alpha,\
                                                        alpha_level=alpha_level,tau_min0=tau_min,tau_max0=tau_max,target='precip',seed=seednum,var_and_lag=var_and_lag)
    wpac_mlr_pmin,X_pmin,y_pmin = func.trainMLR_target(traindata=traindata,validdata=validdata,testdata=testdata,newtestdata=newtestdata,pc_alpha=pc_alpha,\
                                                        alpha_level=alpha_level,tau_min0=tau_min,tau_max0=tau_max,target='pmin',seed=seednum,var_and_lag=var_and_lag)
    wpac_mlr_v10,X_v10,y_v10 = func.trainMLR_target(traindata=traindata,validdata=validdata,testdata=testdata,newtestdata=newtestdata,pc_alpha=pc_alpha,\
                                                        alpha_level=alpha_level,tau_min0=tau_min,tau_max0=tau_max,target='v10',seed=seednum,var_and_lag=var_and_lag)
    
    func.save_to_pickle(loc='./newdata/pcstablewpac_aligned_'+str(tau_min)+'-'+str(tau_max)+'_precip.obj.'+\
                   str(np.round(pc_alpha,decimals=10))+'.'+str(seednum),\
                   var={'mlr':wpac_mlr_precip,'X':X_precip,'y':y_precip})
    
    func.save_to_pickle(loc='./newdata/pcstablewpac_aligned_'+str(tau_min)+'-'+str(tau_max)+'_pmin.obj.'+\
                   str(np.round(pc_alpha,decimals=10))+'.'+str(seednum),\
                   var={'mlr':wpac_mlr_pmin,'X':X_pmin,'y':y_pmin})
    func.save_to_pickle(loc='./newdata/pcstablewpac_aligned_'+str(tau_min)+'-'+str(tau_max)+'_v10.obj.'+\
                  str(np.round(pc_alpha,decimals=10))+'.'+str(seednum),\
                   var={'mlr':wpac_mlr_v10,'X':X_v10,'y':y_v10})
    func.save_to_pickle(loc='./newdata/pcstablewpac_aligned_'+str(tau_min)+'-'+str(tau_max)+'_lag_and_links.'+\
                   str(np.round(pc_alpha,decimals=10))+'.'+str(seednum),var=var_and_lag)
    func.save_to_pickle(loc='./newdata/pcstablewpac_aligned_'+str(tau_min)+'-'+str(tau_max)+'_results.'+\
                   str(np.round(pc_alpha,decimals=10))+'.'+str(seednum),var=saveresults)
print(y_pmin['test'])
