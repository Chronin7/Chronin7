
def ask_questen(type_of_word):
	print("""
adverb: a word that describes and ends in -ly ex: loudly, angrily

adjective: describing word ex: big, smelly

noun: a person place or thing ex: france, hand sanitizer

plural noun: a noun but plural ex: printers, students

verb: an action ex: drive, print

silly word: something that sound funny ex: plorp, sizzle
""")
	return input(f"give me a {type_of_word.lower()}: ")
def madlib():
	libnum=1
	while libnum!=0:
		libnum=input("""i have 13 madlibs 0 to quit, which one would you like to do (0-13): """)
		if libnum=="1": 
			print(f"""All children have {ask_questen("ADJECTIVE")} memories of the books their
	mothers and {ask_questen("pLURAL NOUN")} read to them. Here are some of the all-time {ask_questen("ADJECTIVE")} favorites:
	• The Giving {ask_questen("NOUN")} is a touching story about a friendship
	between a/an {ask_questen("NOUN")} and a tree. Throughout the boy's
	life, the {ask_questen("NOUN")} gives and gives. Kids between the ages of
	{ask_questen("NUMBER")} and {ask_questen("NUMBER")} love this story.
	• Goodnight Moon is a/an {ask_questen("ADJECTIVE")} book that captures
	a child's nightly ritual of saying good night to everything in his
	{ask_questen("NOUN")}. It's great for {ask_questen("pLURAL NOUN")} ages two through six.
	• Written in rhyme, Green Eggs and {ask_questen("TYPE OF FOOD")} made Dr. Seuss
	one of the best-loved children's {ask_questen("pLURAL NOUN")} of all time. While
	many {ask_questen("pLURAL NOUN")} have a moral or a/an {ask_questen("NOUN")}, the lesson
	in this classic is: If you've never tried something, you can't say you
	don't like it. A perfect read for all {ask_questen("ADJECTIVE")} kindergartners""")
		elif libnum=="2":
			print(f"""One of the things most {ask_questen("adJeCtIVe")} sports fans look
	forward to at American baseball {ask_questen("PLUraL NoUN")} is eating a/an
	{ask_questen("adJeCtIVe")} hot dog. There is nothing more traditional
	than watching a/an {ask_questen("adJeCtIVe")} ball game and eating a hot
	{ask_questen("NoUN")} drenched in mustard, relish, and {ask_questen("PLUraL NoUN")}.
	Some {ask_questen("NoUN")}-parks even have their own {ask_questen("adJeCtIVe")}
	specialties, such as the Dodger {ask_questen("NoUN")} in Los Angeles.
	(It's an oversize steamed or grilled {ask_questen("NoUN")}.)
	Hot {ask_questen("PLUraL NoUN")} were created at the end of the nineteenth
	century when a sausage-maker saw his {ask_questen("adJeCtIVe")} customers
	wearing gloves on their {ask_questen("Part of the Body (PLUraL)")} because the
	steaming sausages were too {ask_questen("adJeCtIVe")} to handle. He put
	them in a/an {ask_questen("adJeCtIVe")} roll, and that was the beginning
	of the {ask_questen("adJeCtIVe")} dog in a bun. The rest, as they say, is
	{ask_questen("NoUN")}!""")
		elif libnum=="3":
			print(f"""Thanks to social networking {ask_questen("PLUraL NoUN")} like My-{ask_questen("NoUN")}
	and {ask_questen("Part of the Body")}-book, everyone now has hundreds of
	{ask_questen("adJeCtIVe")} friends. But most people really have only one
	best {ask_questen("NoUN")}. A BFF is someone you tell your deepest,
	most {ask_questen("adJeCtIVe")} secrets to, knowing they won't tell a single
	{ask_questen("NoUN")}. You and your best {ask_questen("NoUN")} can pass
	{ask_questen("PLUraL NoUN")} in class and share a hot fudge {ask_questen("NoUN")} after
	school. And if your {ask_questen("adJeCtIVe")} friend wants some advice on the
	latest {ask_questen("NoUN")} in their life, you'll give them the {ask_questen("adJeCtIVe")}
	truth. And finally, if you ever need a/an {ask_questen("Part of the Body")} to cry
	on, your BFF will be there with a box of {ask_questen("PLUraL NoUN")} and a/an
	{ask_questen("NoUN")} of hot cocoa. Who could {ask_questen("VerB")} for
	anything more?""")	
		elif libnum=="4":
			print(f"""Wow! I bought a new smart-{ask_questen("NoUN")} today. It not only
	makes {ask_questen("NoUN")} calls—it also forecasts the {ask_questen("NoUN")}
	so I know whether to wear a/an {ask_questen("NoUN")} or carry a/an
	{ask_questen("NoUN")} in case it rains cats and {ask_questen("PLUraL NoUN")}.
	It can also read and send e-{ask_questen("PLUraL NoUN")} and even record a
	TV {ask_questen("NoUN")}. And I will never get lost again because I
	now have a global {ask_questen("VerB eNdING IN “ING”")} system that gets me from
	point A to {ask_questen("NoUN")} B in no time. I also received a/an
	{ask_questen("NoUN")}-reader for my birthday. Imagine not only being
	able to download any book in just {ask_questen("NUmBer")} seconds but
	view hundreds of magazines and {ask_questen("PLUraL NoUN")} from all
	over the {ask_questen("NoUN")}. How did we ever get through each
	{ask_questen("adJeCtIVe")} day before these {ask_questen("adJeCtIVe")} inventions?""")
		elif libnum=="5":
			print(f"""Do you remember radio, handwritten letters, and landline
	{ask_questen("PLUraL NoUN")}—all the technology used by your parents to
	communicate with their {ask_questen("PLUraL NoUN")}? These technologies
	are now as old as {ask_questen("NoUN")}. They've been replaced by
	Twitter and {ask_questen("Part of the Body")} -book. Twitter is a great way to stay
	in touch with all your {ask_questen("PLUraL NoUN")} and share {ask_questen("adJeCtIVe")}
	information about what is happening in your own {ask_questen("NoUN")}.
	Just remember to keep it to 140 characters. Facebook is a social
	{ask_questen("VerB eNdING IN “ING”")} service with more than five hundred million
	{ask_questen("PLUraL NoUN")}. You can create a/an {ask_questen("adJeCtIVe")} profile,
	add other {ask_questen("PLUraL NoUN")} as friends, and exchange {ask_questen("adJeCtIVe")}
	messages. Face-{ask_questen("NoUN")} was founded by {ask_questen("PersoN IN room")}
	and a few of his {ask_questen("adJeCtIVe")} college classmates. Social networks
	are popular on the {ask_questen("noun")} Wide Web, where they have
	their own {ask_questen("adJeCtIVe")} language, such as GTG (got to go),
	LOL (laughing out loud), or XOXO (hugs and {ask_questen("PLUraL NoUN")}).""")
		elif libnum=="6":
			print(f"""Although video {ask_questen("PLUraL NoUN")} have been around for over
	{ask_questen("NUmBer")} years, they've become more and more {ask_questen("adJeCtIVe")}
	as developers create more sophisticated {ask_questen("PLUraL NoUN")}. Today's
	{ask_questen("NoUN")} games are so complicated, they require really
	{ask_questen("adJeCtIVe")} attention at all times. They have you sitting
	on pins and {ask_questen("PLUraL NoUN")} throughout the entire game. Such
	{ask_questen("PLUraL NoUN")} as Final {ask_questen("NoUN")} XIII, Grand Theft
	{ask_questen("NoUN")}, and (the) {ask_questen("place")} Noire cost more
	to develop than many {ask_questen("adJeCtIVe")} movies produced by big
	Hollywood {ask_questen("PLUraL NoUN")}. If the technology in the video-gaming
	{ask_questen("noun")} continues to advance, imagine what future electronic
	{ask_questen("PLUraL NoUN")} will be like. It's {ask_questen("noun")}-boggling.""")
		elif libnum=="7":
			print(f"""Our Fourth of July started out {ask_questen("ADJECTIVE")} enough. Aunt
	{ask_questen("PERSON IN ROOM (FEMALE)")} and Uncle {ask_questen("PERSON IN ROOM (MALE)")} were coming
	over to spend the day with my family. We had a really {ask_questen("ADJECTIVE")}
	barbecue set up in the backyard, with lots of {ask_questen("TYPE OF FOOD (PLURAL)")}
	and {ask_questen("PLURAL NOUN")} right off the grill. The trouble started when
	my aunt and uncle arrived and we found out they had brought
	along the newest and most {ask_questen("ADJECTIVE")} member of their family:
	a/an {ask_questen("NUMBER")} -pound pet pig named {ask_questen("CELEBRITY (MALE)")}!
	The pig looked {ask_questen("ADJECTIVE")} enough, and he even made a noise
	that sounded like “{ask_questen("EXCLAMATION")}!” when I petted him on
	his {ask_questen("PART OF THE BODY")}. But when we put him in the backyard to
	{ask_questen("VERB")}, everything got totally out of hand! The pig took one
	sniff of all the {ask_questen("ADJECTIVE")} food and started to {ask_questen("VERB")} around
	like crazy. He knocked over all the tables and {ask_questen("PLURAL NOUN")}, destroyed
	my kid sister's playhouse, and took a swim in the {ask_questen("TYPE OF LIQUID")}.
	“That's it!” my father yelled. “Next time you bring a/an {ask_questen("ANIMAL ")}
	to a barbecue, we're going to cook him!”""")
		elif libnum=="8":
			print(f"""My best {ask_questen("NOUN")}, {ask_questen("PERsON IN ROOM ")}, is a pro at serving detentions
	and suggests bringing the following items to make it through the hour:
	• A/An {ask_questen("NOUN")} phone—but don't use it for
	{ask_questen("VERB ENDINg IN “INg”")}; instead, use it as a watch, a calculator, or a/
	an {ask_questen("NOUN")}. And be sure to turn it to “{ask_questen("VERB")}”
	so it doesn't ring.
	• An i-{ask_questen("NOUN")} to listen to music. Cover up the
	{ask_questen("PART OF THE BODY")}-phones by wearing a hooded {ask_questen("NOUN")} .
	• Some tissues, in case you need to blow your {ask_questen("PART OF THE BODY")}
	• Blank paper and something to {ask_questen("VERB")} with. Use
	these {ask_questen("ADJECTIVE")} items to compose love songs to your
	crush, {ask_questen("PERsON IN ROOM")}, draw a comic strip featuring
	{ask_questen("PERsON IN ROOM")} as the underwear-wearing superhero Captain
	{ask_questen("NOUN")}-pants, or even do something crazy, like your
	{ask_questen("NOUN")} homework
	• A pair of {ask_questen("NOUN")}-glasses—you might as well look
	{ask_questen("ADJECTIVE")} while you're there!""")
		elif libnum=="9":
			print(f"""Pack your bags! It's time to take a/an {ask_questen("ADJECTIVE")} road trip across
	the United States to visit some of the most {ask_questen("ADJECTIVE")} historical
	landmarks. First stop is Philadelphia, where you can visit Independence
	Hall to see where the Declaration of {ask_questen("PLURAL NOUN")} was signed. After
	that, check out the Liberty Bell. It's the most famous cracked
	{ask_questen("NOUN")} in history, and a symbol of freedom across America.
	Then head on up to Boston, where you can check out the USS
	Constitution, the oldest {ask_questen("VERB ENDINg IN “INg”")} naval vessel, and the
	{ask_questen("NOUN")} Hill Monument. In New York, you can climb to the
	top of the {ask_questen("NOUN")} of Liberty (or take a/an {ask_questen("VEHICLE")} to
	check out the view from the harbor!). Now it's time to head west, where
	you can see famous landmarks like Mount {ask_questen("SILLY WORD")}, which
	features carved statues of the {ask_questen("PART OF THE BODY (PLURAL)")} of some of our
	most {ask_questen("ADJECTIVE")} presidents. Or check out {ask_questen("COLOR")}-stone,
	our first national park, which includes the famous geyser Old
	{ask_questen("ADJECTIVE")} ! Just don't forget to pack a/an {ask_questen("NOUN")}—you'll
	want to take pictures to remember your {ask_questen("ADJECTIVE")} trip by!""")
		elif libnum=="10":
			print(f"""Are you a king, queen, or {ask_questen("OccUPAtION")} looking for that perfectly
	{ask_questen("AdjEctIvE")} new home? Then have we got a/an {ask_questen("AdjEctIvE")}
	place for you! King {ask_questen("PERSON IN ROOM (MALE)")} 's {ask_questen("AdjEctIvE")} castle
	has just come on the market! Originally built in the {ask_questen("AdjEctIvE")}
	Ages, this lakefront wonder has towers that rise high above (the)
	{ask_questen("place")} and a/an {ask_questen("AdjEctIvE")} view that will take your
	{ask_questen("PARt OF tHE BOdY")} away. In each and every room of this 25,000 square-
	{ask_questen("PARt OF tHE BOdY")} masterpiece, there are magnificent stained glass
	{ask_questen("PLURAL NOUN")} and splendid Gothic {ask_questen("NOUN")}-burning
	fireplaces. There's also a chef's state-of-the-art, {ask_questen("AdvERB")}
	modern {ask_questen("NOUN")} for those who love to {ask_questen("vERB")}.
	For security and {ask_questen("AdjEctIvE")} privacy, there is also a moat filled
	with {ask_questen("PLURAL NOUN")} and a drawbridge to keep out unwanted
	{ask_questen("PLURAL NOUN")}. Take advantage of the collapse in the castle
	market and make a/an {ask_questen("AdjEctIvE")} offer on this treasure. The
	asking price is a ridiculously low {ask_questen("NUMBER")} dollars. """)
		elif libnum=="11":
			the_odd_one=""
			the_odd_one=ask_questen("animal")
			print(f"""It is difficult not to envy a young woman who has everything her
	{ask_questen("PARt OF tHE BOdY")} desires. But history shows it isn't easy being a
	princess. You have to maintain {ask_questen("AdjEctIvE")} standards and abide
	by {ask_questen("AdjEctIvE")} rules. For example:
	• A princess should always be kind to, and understanding of, her
	royal {ask_questen("PLURAL NOUN")} . A princess knows that a/an {ask_questen("AdjEctIvE")}
	smile is preferable to a/an {ask_questen("AdjEctIvE")} frown.
	• A princess should be a patron of the arts, well-versed in classical
	{ask_questen("NOUN")} , and {ask_questen("AdvERB")} familiar with
	{ask_questen("AdjEctIvE")} authors and their {ask_questen("AdjEctIvE")} works.
	• A princess should never make a/an {ask_questen("AdjEctIvE")} decision. She
	should always think before {ask_questen("vERB ENdING IN “ING”")} . And when she
	does speak, she should be articulate and, if possible, very
	{ask_questen("AdjEctIvE")} .
	• And, of course, a princess must be prepared to marry a/an
	{ask_questen("AdjEctIvE")} prince and live {ask_questen("AdvERB")} ever after.""")
		elif libnum=="12":
			print(f"""It's summer, and you know what that means: {ask_questen("ADJECTIVE")}
	weather, icy-cold {ask_questen("NOUN")}-sicles, and big blockbusters. Check
	out what's coming to a/an {ask_questen("NOUN")} near you this summer!
	• {ask_questen("PLURAL NOUN")} of the Caribbean: Captain {ask_questen("PERSON IN ROOM (MALE)")}
	and his band of {ask_questen("ADJECTIVE")} scalawags take to the {ask_questen("ADJECTIVE")}
	seas in search of buried {ask_questen("PLURAL NOUN")}.
	• The Big {ask_questen("ADJECTIVE")} Ogre: A cranky ogre named
	{ask_questen("PERSON IN ROOM (MALE)")}, his sidekick—a/an {the_odd_one}
	named {the_odd_one}—and a/an {ask_questen("ADJECTIVE")} gang of
	fairy tale creatures go on a search and {ask_questen("VERB")} mission to
	rescue Princess {ask_questen("PERSON IN ROOM (FEMALE)")} from a tower guarded by a firebreathing {ask_questen("NOUN")}.
	• The Boy Wizard: A/An {ask_questen("ADJECTIVE")} boy discovers he
	possesses magical {ask_questen("PLURAL NOUN")} that he must use to defeat the
	evil wizard, Lord {ask_questen("PERSON IN ROOM (MALE)")}.""")
		elif libnum=="13":
			print(f"""Are you cheery and {ask_questen("PLURAL NOUN")} at the crack of dawn? Do you
	leap out of bed early in the morning, ready to greet the world with
	a dazzling {ask_questen("ADVERB")}? As a journalist, can you quickly switch
	gears from interviewing the ruler of (the) {ask_questen("VERB")} to quizzing
	an expert on the effects of global {ask_questen("ARTICLE OF CLOTHING")} on the planet to
	judging a beauty contest for {ask_questen("BODY PART")}? Then you could
	be the {ask_questen("ADJECTIVE")} morning show host we're looking for! The
	number one-ranked show Good Morning, {ask_questen("NOUN")} is
	searching for a cohost to join the current host, {ask_questen("PLURAL NOUN")}.
	The show combines {ask_questen("ANOTHER BODY PART")}, hard news stories with lighter
	pieces such as cooking and {ask_questen("PLURAL NOUN")} segments, interviews
	with A-listers like {ask_questen("ANOTHER BODY PART")} and {ask_questen("NOUN")}, and
	fashion tips such as one hundred stylish ways to wear a feathered
	{ask_questen("NOUN")}. Salary is {ask_questen("VERB ENDING IN “ING”")} a year plus a
	generous allowance for clothing and {ask_questen("ADJECTIVE")}. Are you
	qualified? Then {ask_questen("VERB")} today for an application!""")
		elif libnum=="0":
			return