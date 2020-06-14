import socket
import random, threading
from ftplib import FTP
print("""
  ___   _      ___   _      ___   _      ___   _      ___   _
 [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|
  '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|
       |____________|____________|____________|____________|
                             | _          | _          | _
Search for servers      [(_)] |=|    [(_)] |=|    [(_)] |=|
             the world   '-`  |_|     '-`  |_|     '-`  |_|

               | Termux-Lab | t.me/termuxlab |
""")
while True:
    port = input("[Port]# ")
    if port == "?":
        print("""
0/TCP,UDP 	резерв (допустимо использование в качестве значения порта источника, если отправляющий процесс не ожидает ответных сообщений) 	Официально

1/TCP,UDP 	TCPMUX (TCP Port Service Multiplexer) — для обслуживания нескольких служб через один TCP-порт 	Официально

2/TCP,UDP 	COMPRESSNET, процесс управления 	Официально

3/TCP,UDP 	COMPRESSNET, процесс сжатия 	Официально

5/TCP,UDP 	RJE (Remote Job Entry) — обслуживает отправку файлов и вывод отчётов при работе рабочей станции с мейнфреймами 	Официально

7/TCP,UDP 	ECHO — предназначен для тестирования связи путём отправки данных на сервер и получения от него их же в неизменном виде 	Официально

9/TCP,UDP 	DISCARD — предназначен для тестирования связи путём отправки данных на сервер, который отбрасывает принятое, не отправляя никакого ответа. Также используется для Wake-on-LAN-удалённого включения компьютера. 	Официально

11/TCP,UDP 	SYSTAT — выдаёт список активных пользователей в операционной системе 	Официально

13/TCP,UDP 	DAYTIME — предназначен для тестирования связи путём получения от сервера текущих даты и времени в текстовом виде 	Официально

15/TCP 	не назначено; ранее — NETSTAT 	Неофициально

17/TCP,UDP 	QOTD (Quote of the Day) 	Официально

18/TCP,UDP 	MSP (Message Send Protocol)[en] 	Официально

19/TCP,UDP 	CHARGEN (Character Generator) 	Официально

20/TCP 	FTP-DATA — для передачи данных FTP 	Официально

21/TCP 	FTP — для передачи команд FTP 	Официально

22/TCP,UDP 	SSH (Secure SHell) — криптографический сетевой протокол для безопасной передачи данных 	Официально

23/TCP,UDP 	Telnet — применяется для передачи текстовых сообщений в незашифрованном виде 	Официально

24/TCP,UDP 	PRIV-MAIL — для использования в любых частных системах пересылки почтовых сообщений 	Официально

25/TCP,UDP 	SMTP (Simple Mail Transfer Protocol) — применяется для пересылки почтовых сообщений в виде незашифрованного текста 	Официально

26/TCP,UDP 	RSFTP — упрощенный аналог протокола FTP 	Неофициально

26/UDP 	использовался в игре Dungeon Siege II 	Неофициально

27/TCP,UDP 	NSW-FE (NSW User System FE) 	Официально

29/TCP,UDP 	MSG-ICP 	Официально

31/TCP,UDP 	MSG-AUTH 	Официально

33/TCP,UDP 	DSP (Display Support Protocol) 	Официально

35/TCP,UDP 	PRIV-PRINT — для использования любыми частными серверами печати 	Официально

35/UDP 	использовался в игре Delta Force 	Неофициально

37/TCP,UDP 	TIME[en] — используется для синхронизации времени (устар.) 	Официально

38/TCP,UDP 	RAP (Route Access Protocol) 	Официально

39/TCP,UDP 	RLP (Resource Location Protocol)[1], протокол поиска ресурсов — служит для нахождения серверов, предоставляющих услуги верхнего уровня 	Официально

41/TCP,UDP 	Graphics — используется графическими модулями некоторых браузерных программ 	Официально

42/TCP,UDP 	NAME, NAMESERVER — ARPA Host Name Server Protocol[en], протокол сервера имён ARPA (устар.) 	Официально

42/TCP,UDP 	WINS (Windows Internet Name Service) — в настоящее время считается устаревшим 	Неофициально

43/TCP,UDP 	WHOIS 	Официально

44/TCP,UDP 	MPM-FLAGS (Message Processing Module, Flags) 	Официально

45/TCP,UDP 	MPM (Message Processing Module, receive) 	Официально

46/TCP,UDP 	MPM-SND (Message Processing Module, send) 	Официально

47/TCP,UDP 	NI-FTP 	Официально

48/TCP,UDP 	AUDITD (Digital Audit Daemon) 	Официально

49/TCP,UDP 	TACACS Login Host protocol 	Официально

50/TCP,UDP 	RE-MAIL-CK 	Официально

51/TCP,UDP 	резерв; ранее — LA-MAINT (IMP Logical Address Maintenance) 	Официально

52/TCP,UDP 	XNS-TIME (Xerox Network Services Time Protocol) 	Официально

53/TCP,UDP 	DOMAIN (Domain Name System, DNS) 	Официально

54/TCP,UDP 	XNS-CH (Xerox Network Services ClearingHouse) 	Официально

55/TCP,UDP 	ISI-GL (ISI Graphics Language)[2] 	Официально

56/TCP,UDP 	XNS-AUTH (Xerox Network Services Authentication) 	Официально

56/TCP,UDP 	RAP (Route Access Protocol)[3] 	Неофициально

57/TCP,UDP 	PRIV-TERM — для любых служб, обеспечивающих терминальный доступ; ранее — MTP (Mail Transfer Protocol[en]) 	Официально

58/TCP,UDP 	XNS-MAIL (Xerox Network Services Mail) 	Официально

59/TCP,UDP 	PRIV-FILE — для любых служб обработки файлов 	Официально

61/TCP,UDP 	NI-MAIL 	Официально

62/TCP,UDP 	ACAS (ACA Services) 	Официально

63/TCP,UDP 	WHOISPP 	Официально

64/TCP,UDP 	COVIA 	Официально

65/TCP,UDP 	TACACS-DS (TACACS Database Service) 	Официально

66/TCP,UDP 	SQL-NET 	Официально

67/TCP,UDP 	BOOTPS (Bootstrap Protocol Server) — для сервера, с которого выполняется загрузка бездисковых рабочих станций; также используется DHCP (Dynamic Host Configuration Protocol) 	Официально

68/TCP,UDP 	BOOTPC (Bootstrap Protocol Client) — для клиентов бездисковых рабочих станций, загружающихся с сервера BOOTP; также используется DHCP (Dynamic Host Configuration Protocol) 	Официально

69/TCP,UDP 	TFTP (Trivial File Transfer Protocol) — тривиальный FTP применяется, например, при установке операционной системы на большое количество компьютеров в сетях предприятий. Для этого сервер TFTP и поддержка удалённого развёртывания (UAM) включены в состав серверных ОС Windows NT4 Server и новее 	Официально

70/TCP,UDP 	Gopher 	Официально

71/TCP,UDP 	NETRJS-1 (Remote job entry[en] Service) 	Официально

72/TCP,UDP 	NETRJS-2 (Remote job entry[en] Service) 	Официально

73/TCP,UDP 	NETRJS-3 (Remote job entry[en] Service) 	Официально

74/TCP,UDP 	NETRJS-4 (Remote job entry[en] Service) 	Официально

75/TCP,UDP 	PRIV-DIAL — для любых приложений телефонного дозвона 	Официально

76/TCP,UDP 	DEOS (Distributed External Object Store) 	Официально

77/TCP,UDP 	PRIV-RJE — для использования в любых службах Remote Job Entry[en] 	Официально

78/TCP,UDP 	VETTCP 	Официально

79/TCP,UDP 	Finger 	Официально

80/TCP,UDP 	HTTP (HyperText Transfer Protocol); ранее — WWW 	Официально

81/TCP 	HTTP (HyperText Transfer Protocol) 	Неофициально

81/TCP 	используется в приложениях проекта Tor для целей маршрутизации 	Неофициально

81/TCP,UDP 	HOSTS2-NS (HOSTS2 Name Server) 	Неофициально

82/TCP,UDP 	XFER 	Официально

82/UDP 	используется в приложениях проекта Tor для целей управления 	Неофициально

83/TCP,UDP 	MIT-ML-DEV (MIT ML Device) 	Официально

84/TCP,UDP 	CTF (Common Trace Facility) 	Официально

85/TCP,UDP 	MIT-ML-DEV (MIT ML Device) 	Официально

86/TCP,UDP 	MFCOBOL (Micro Focus Cobol) 	Официально

87/TCP,UDP 	PRIV-TERM-L — для любых приложений, обеспечивающих терминальное соединение типа «текстовый чат» (например, аналогичных talk) 	Официально

88/TCP,UDP 	Система аутентификации Kerberos 	Официальн

89/TCP,UDP 	SU-MIT-TG (SU/MIT Telnet Gateway) 	Официально

90/TCP,UDP 	DNSIX (DoD Network Security for Information eXchange) Securit Attribute Token Map 	Неофициально

90/TCP,UDP 	PointCast[en] 	Неофициально

91/TCP,UDP 	MIT-DOV (MIT Dover Spooler) 	Официально

92/TCP,UDP 	NPP (Network Printing Protocol) 	Официально

93/TCP,UDP 	DCP (Device Control Protocol) 	Официально

94/TCP,UDP 	OBJCALL 	Официально

95/TCP,UDP 	SUPDUP 	Официально

96/TCP,UDP 	DIXIE 	Официально

97/TCP,UDP 	SWIFT-RVF (Swift Remote Virtural File Protocol) 	Официально

98/TCP,UDP 	TACNEWS 	Официально

98/TCP 	LINUXCONF 	Неофициально

99/TCP,UDP 	METAGRAM 	Официально

100/TCP 	NEWACCT

101/TCP,UDP 	HOSTNAME (NIC[en] Host Name Server) 	Официально

102/TCP,UDP 	ISO-TSAP (Transport Service Access Point[en] Class 0)[4] 	Официально

103/TCP,UDP 	GPPITNP (Genesis Point-to-Point Trans Net) 	Официально

104/TCP,UDP 	ACR-NEMA (ACR/NEMA DICOM) 	Официально

105/TCP,UDP 	CSO, CSNET-NS (CCSO[en]/Mailbox Name Nameserver) 	Официально

106/TCP,UDP 	3COM-TSMUX 	Официально

107/TCP,UDP 	RTELNET (Remote Telnet Service[5]) 	Официально

108/TCP,UDP 	SNAGAS (SNA Gateway Access Server) 	Официально

109/TCP,UDP 	POP2 (Post Office Protocol Version 2) 	Официально

110/TCP,UDP 	POP3 (Post Office Protocol Version 3) 	Официально

110/UDP 	использовался в игре Final Fantasy XI 	Неофициально

111/TCP,UDP 	SUNRPC (Sun Remote Procedure Call) 	Официально

112/TCP,UDP 	MCIDAS (McIDAS Data Transmission) 	Официально

113/TCP,UDP 	AUTH (Authentication Service) 	Официально

113/TCP 	IDENT — старая система идентификации, до сих пор используется в IRC-серверах 	Официально

114/TCP,UDP 	AUDIONEWS (Audio News Multicast) 	Неофициально

115/TCP,UDP 	SFTP (Simple File Transfer Protocol[en]) 	Официально

116/TCP,UDP 	ANSANOTIFY (ANSA REX Notify) 	Официально

117/TCP,UDP 	UUCP-PATH (UUCP Path Service) 	Официально

118/TCP,UDP 	SQLSERV (SQL Services) 	Официально

119/TCP,UDP 	NNTP (Network News Transfer Protocol) — используется для отправки сообщений новостных рассылок 	Официально

120/TCP,UDP 	CFDPTKT (RFC 1235) 	Официально

121/TCP,UDP 	ERPC (Encore Expedited Remote Protocol Call) 	Официально

122/TCP,UDP 	SMAKYNET 	Официально

123/TCP,UDP 	NTP (Network Time Protocol) — используется для синхронизации времени 	Официально

124/TCP,UDP 	ANSATRADER (ANSA REX Trader) 	Официально

125/TCP,UDP 	LOCUS-MAP (Locus PC-Interface Net Map Ser) 	Официально

125/TCP 	используется как альтернатива порту 25/TCP (SMTP) 	Неофициально

126/TCP,UDP 	NXEdit; ранее — Unisys Unitary Login 	Официально

127/TCP,UDP 	LOCUS-CON (Locus PC-Interface Conn Server) 	Официально

127/UDP 	использовался в игре Command and Conquer Generals 	Неофициально

128/TCP,UDP 	GSS-XLICEN (GSS X License Verification) 	Официально

129/TCP,UDP 	PWDGEN (Password Generator Protocol) 	Официально

130/TCP,UDP 	CISCO-FNA (Cisco FNATIVE) 	Официально

131/TCP,UDP 	CISCO-TNA (Cisco TNATIVE) 	Официально

132/TCP,UDP 	CISCO-SYS (Cisco SYSMAINT) 	Официально

133/TCP,UDP 	STATSRV (Statistics Service) 	Официально

134/TCP,UDP 	INGRES-NET 	Официально

135/TCP,UDP 	EPMAP (DCE[en] Endpoint Mapper) 	Официально

135/TCP,UDP 	MSRPC (Microsoft RPC[6]) — используется в приложениях «клиент—сервер» Microsoft (например, Exchange) 	Неофициально

135/TCP,UDP 	LOC-SRV (Locator service) — используется службами удалённого обслуживания (DHCP, DNS, WINS и т. д.) 	Неофициально

136/TCP,UDP 	PROFILE Naming System 	Официально

137/TCP,UDP 	NETBIOS-NS (NetBIOS Name Service) 	Официально

138/TCP,UDP 	NETBIOS-DGM (NetBIOS Datagram Service) 	Официально

139/TCP,UDP 	NETBIOS-SSN (NetBIOS Session Service) 	Официально

140/TCP,UDP 	EMFIS-DATA (EMFIS Data Service) 	Официально

141/TCP,UDP 	EMFIS-CNTL (EMFIS Control Service) 	Официально

142/TCP,UDP 	BL-IDM (Britton-Lee IDM) 	Официально

143/TCP,UDP 	IMAP (Internet Message Access Protocol) — используется для получения и синхронизации сообщений электронной почты 	Официально

144/TCP,UDP 	UMA (Universal Management Architecture) 	Официально

144/TCP,UDP 	NEWS 	Неофициально

145/TCP,UDP 	UAAC 	Официально

146/TCP,UDP 	ISO-TP0 	Официально

147/TCP,UDP 	ISO-IP 	Официально

148/TCP,UDP 	JARGON 	Официально

148/TCP,UDP 	CRONUS 	Неофициально

149/TCP,UDP 	AED-512 	Официально

150/TCP,UDP 	SQL-NET 	Официально

151/TCP,UDP 	HEMS 	Официально

152/TCP,UDP 	BFTP (Background File Transfer Program)[7] 	Официально

153/TCP,UDP 	SGMP (Simple Gateway Monitoring Protocol[en]) 	Официально

154/TCP,UDP 	NETSC-PROD 	Официально

155/TCP,UDP 	NETSC-DEV 	Официально

156/TCP,UDP 	SQLSRV (SQL Service) 	Официально

157/TCP,UDP 	KNET-CMP 	Официально

158/TCP,UDP 	PCMAIL-SRV 	Официально

158/TCP,UDP 	DMSP (Distributed Mail Service Protocol) 	Неофициально

159/TCP,UDP 	NSS-ROUTING 	Официально

160/TCP,UDP 	SGMP-TRAPS 	Официально

161/TCP,UDP 	SNMP (Simple Network Management Protocol) — используется как порт прослушивания агентами удалённого мониторинга 	Официально

162/TCP,UDP 	SNMPTRAP (Simple Network Management Protocol Trap)[8] — используется как порт приёма асинхронных прерываний (traps) 	Официально

163/TCP,UDP 	CMIP-MAN (CMIP/TCP Manager) 	Официально

164/TCP,UDP 	CMIP-AGENT (CMIP/TCP Agent) 	Официально

165/TCP,UDP 	XNS-COURIER (Xerox Network Services) 	Официально

166/TCP,UDP 	S-NET (Sirius Systems Network) 	Официально

167/TCP,UDP 	NAMP 	Официально

168/TCP,UDP 	RSVD 	Официально

169/TCP,UDP 	SEND 	Официально

170/TCP,UDP 	PRINT-SRV (Network PostScript) 	Официально

171/TCP,UDP 	MULTIPLEX (Network Innovations Multiplex) 	Официально

172/TCP,UDP 	CL-1 (Network Innovations CL/1); ранее — CL/1 	Официально

173/TCP,UDP 	XYPLEX-MUX 	Официально

174/TCP,UDP 	MAILQ 	Официально

175/TCP,UDP 	VMNET 	Официально

176/TCP,UDP 	GENRAD-MUX 	Официально

177/TCP,UDP 	XDMCP (X Display Manager Control Protocol) 	Официально

178/TCP,UDP 	NEXTSTEP (NextStep Window Server) 	Официально

179/TCP,UDP 	BGP (Border Gateway Protocol) 	Официально

180/TCP,UDP 	RIS (Intergraph) 	Официально

181/TCP,UDP 	UNIFY 	Официально

182/TCP,UDP 	AUDIT (Unisys Audit SITP) 	Официально

183/TCP,UDP 	OCBINDER 	Официально

184/TCP,UDP 	OCSERVER 	Официально

185/TCP,UDP 	REMOTE-KIS 	Официально

186/TCP,UDP 	KIS 	Официально

187/TCP,UDP 	ACI (Application Communication Interface) 	Официально

188/TCP,UDP 	MUMPS 	Официально

189/TCP,UDP 	QFT (Queued File Transport) 	Официально

190/TCP,UDP 	GACP (Gateway Access Control Protocol) 	Официально

191/TCP,UDP 	PROSPERO (Prospero Directory Service) 	Официально

192/TCP,UDP 	OSU-NMS (OSU Network Monitoring System) 	Официально

193/TCP,UDP 	SRMP (Spider Remote Monitoring Protocol) 	Официально

194/TCP,UDP 	IRC (Internet Relay Chat) 	Официально

195/TCP,UDP 	DN6-NLM-AUD (DNSIX Network Level Module Audit) 	Официально

196/TCP,UDP 	DN6-SMM-RED (DNSIX Session Mgt Module Audit Redir) 	Официально

197/TCP,UDP 	DLS (Directory Location Service) 	Официально

198/TCP,UDP 	DLS-MON (Directory Location Service Monitor) 	Официально

199/TCP,UDP 	SMUX (SNMP Unix Multiplexer) 	Официально

200/TCP,UDP 	SRC (IBM System Resource Controller) 	Официально

201/TCP,UDP 	AT-RTMP (AppleTalk Routing Maintenance) 	Официально

202/TCP,UDP 	AT-NBP (AppleTalk Name Binding) 	Официально

203/TCP,UDP 	AT-3 (AppleTalk Unused) 	Официально

204/TCP,UDP 	AT-ECHO (AppleTalk Echo) 	Официально

205/TCP,UDP 	AT-5 (AppleTalk Unused) 	Официально

206/TCP,UDP 	AT-ZIS (AppleTalk Zone Information) 	Официально

207/TCP,UDP 	AT-7 (AppleTalk Unused) 	Официально

208/TCP,UDP 	AT-8 (AppleTalk Unused) 	Официально

209/TCP,UDP 	QMTP (The Quick Mail Transfer Protocol) 	Официально

210/TCP,UDP 	Z39-50 (ANSI Z39.50) 	Официально

211/TCP,UDP 	914C-G (Texas Instruments 914C/G Terminal) 	Официально

212/TCP,UDP 	ANET (ATEXSSTR) 	Официально

213/TCP,UDP 	IPX 	Официально

214/TCP,UDP 	VMPWSCS 	Официально

215/TCP,UDP 	SOFTPC (Insignia Solutions) 	Официально

216/TCP,UDP 	CALLIC (Computer Associates Int’l License Server) 	Официально

216/TCP,UDP 	ATLS (Access Technology License Server) 	Неофициально

217/TCP,UDP 	DBASE (dBASE Unix) 	Официально

218/TCP,UDP 	MPP (Message Posting Protocol) 	Официально

219/TCP,UDP 	UARPS (Unisys ARPs) 	Официально

220/TCP,UDP 	IMAP3 (Interactive Mail Access Protocol, version 3) 	Официально

221/TCP,UDP 	FLN-SPX (Berkeley rlogind with SPX auth) 	Официально

222/TCP,UDP 	RSH-SPX (Berkeley rshd with SPX auth) 	Официально

223/TCP,UDP 	CDC (Certificate Distribution Center) 	Официально

224/TCP,UDP 	MASQDIALER 	Официально

242/TCP,UDP 	DIRECT 	Официально

243/TCP,UDP 	SUR-MEAS (Survey Measurement) 	Официально

244/TCP,UDP 	INBUSINESS 	Официально

245/TCP,UDP 	LINK 	Официально

246/TCP,UDP 	DSP3270 (Display Systems Protocol) 	Официально

247/TCP,UDP 	SUBNTBCST-TFTP 	Официально

248/TCP,UDP 	BHFHS 	Официально

249/TCP,UDP 	резерв 	Официально

250/TCP,UDP 	резерв 	Официально

251/TCP,UDP 	резерв 	Официально

252/TCP,UDP 	резерв 	Официально

253/TCP,UDP 	резерв 	Официально

254/TCP,UDP 	резерв 	Официально

255/TCP,UDP 	резерв 	Официально

256/TCP,UDP 	RAP 	Официально

256/TCP 	FW1-SYNC (Checkpoint FW-1 state table sync) 	Неофициально

257/TCP,UDP 	SET (Secure Electronic Transaction) 	Официально

257/TCP 	FW1-LOG (Checkpoint FW-1 log transfer) 	Неофициально

258/TCP 	FW1-MC (Checkpoint FW-1 management console) 	Неофициально

258/UDP 	YAK-CHAT (Yak Winsock Personal Chat) 	Неофициально

259/TCP,UDP 	ESRO-GEN (Efficient Short Remote Operations) 	Официально

259/UDP 	FW1-RDP (Checkpoint FW-1 RDP) 	Неофициально

260/TCP,UDP 	OPENPORT 	Официально

260/UDP 	FW1-SNMP (Checkpoint FW-1 SNMP agent) 	Неофициально

261/TCP,UDP 	NSIIOPS (IIOP Name Service over TLS/SSL) 	Официально

261/TCP 	FW1-MGMT (Checkpoint FW-1 management) 	Неофициально

262/TCP,UDP 	ARCISDMS 	Официально

263/TCP,UDP 	HDAP 	Официально

264/TCP,UDP 	BGMP (Border Gateway Multicast Protocol[en]) 	Официально

264/TCP 	FW1-TOPO (Checkpoint FW-1 topology download) 	Неофициально

265/TCP,UDP 	X-BONE-CTL 	Официально

265/TCP 	FW1-KEY (Checkpoint FW-1 public key transfer protocol) 	Неофициально

266/TCP,UDP 	SST (SCSI on ST) 	Официально

267/TCP,UDP 	TD-SERVICE (Tobit David Service Layer) 	Официально

268/TCP,UDP 	TD-REPLICA (Tobit David Replica) 	Официально

269/TCP,UDP 	MANET 	Официально

270/TCP 	резерв 	Официально

270/UDP 	GIST (Q-mode encapsulation for GIST messages) 	Официально

271/TCP 	PT-TLS (IETF Network Endpoint Assessment/NEA Posture Transport Protocol over TLS) 	Официально

271/UDP 	резерв 	Официально

280/TCP,UDP 	HTTP-MGMT 	Официально

281/TCP,UDP 	PERSONAL-LINK 	Официально

282/TCP,UDP 	CABLEPORT-AX (Cable Port A/X) 	Официально

283/TCP,UDP 	RESCAP 	Официально

284/TCP,UDP 	CORERJD 	Официально

286/TCP,UDP 	FXP (FXP Communication) 	Официально

287/TCP,UDP 	K-BLOCK 	Официально

308/TCP,UDP 	NOVASTORBAKCUP (Novastor Backup) 	Официально

309/TCP,UDP 	ENTRUSTTIME 	Официально

310/TCP,UDP 	BHMDS
...
        """)
    else:
        break
th = input("[Threading]# ")
print("Search...")
def potoc (name):
    while True:
        target = str(random.randint(1,225))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))+"."+str(random.randint(0,255))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target,int(port)))
        if(result == 0):
            print("_"*(len(target)+len(port)+2))
            print(""+target+":"+str(port)+"")
            if str(port)=='21':
                try:
                    ftp = FTP()
                    ftpx = ftp.connect(target, int(port))
                    save_file = open(port+".log", "a+")
                    save_file.write(""+target+":"+str(port)+"\n"+ftpx+"\n\n\n")
                    save_file.close()
                    print(ftpx)
                except:
                    save_file = open(port+".log", "a+")
                    save_file.write(""+target+":"+str(port)+"\n\n\n")
                    save_file.close()

        sock.close()
for i in range(int(th)):
    x = threading.Thread(target=potoc, args=(i,))
    x.start()
x.join()
