
'''
The DevSecOps Playbook -OREILY




CHAPTER 1: Introducing DevSecOps
1.1: WHY DEVSECOPS? WHY NOW?
1.2: DevOps OVERVIEW
1.3: DevSecOps OVERVIEW
1.4: RUGGED DevOps OVERVIEW
1.5:DevSecOps BUSINESS RESULTS
    CONCLUSION
    NOTES

CHAPTER 2: The Evolution of Cybersecurity (from Perimeter to Zero Trust)
2.1: THE EVOLUTION OF THE THREAT LANDSCAPE
2.2: THE EVOLUTION OF CYBERSECURITY RESPONSE
    CONCLUSION
    NOTES

CHAPTER 3: DevSecOps People
3.1: INTRODUCTION
3.2: COLLABORATION AT THE CORE
3.3: DevSecOps CULTURE
3.4: THE SHARED RESPONSIBILITY MODEL
3.5: PSYCHOLOGICAL SAFETY
3.6: ORGANIZING FOR DevSecOps
3.7: BUILDING A DevSecOps CULTURE
3.8: THE EVOLUTION OF THE EMPLOYEE (T‐SHAPED PEOPLE)
3.9: HIRING FOR DevSecOps
    CONCLUSION
    NOTES

CHAPTER 4: DevSecOps Process
4.1: INTRODUCTION
4.2: UNDERSTANDING PROCESSES AT SCALE
4.3: DevSecOps FOR IT SERVICE MANAGEMENT
4.4: SECURITY INCIDENT MANAGEMENT
4.5: CHANGE MANAGEMENT
4.6: PROBLEM MANAGEMENT
4.7: RELEASE MANAGEMENT
4.8: A DevOps APPROACH TO SECURITY PROCESSES
4.9: CHAOS ENGINEERING
    CONCLUSION
    NOTES

CHAPTER 5: DevSecOps Technology
5.1: INTRODUCTION
5.2: DevSecOps CONTINUOUS INTEGRATION AND CONTINUOUS DEPLOYMENT
5.3: INFRASTRUCTURE AS CODE
5.4: SECRETS MANAGEMENT
5.5: PRIVILEGED ACCESS MANAGEMENT
5.6: RUNTIME APPLICATION SELF‐PROTECTION
5.7: MONITORING AND OBSERVABILITY
5.8: EVENT MANAGEMENT WITH SIEM AND SOAR
    CONCLUSION
    NOTES

CHAPTER 6: DevSecOps Governance
6.1: INTRODUCTION
6.2: THE CHALLENGE OF COMPLIANCE
6.3: MANAGING RISK
6.4: DevSecOps APPROACH TO GOVERNANCE
6.5: COMPLIANCE AS CODE
6.6: COMPLIANCE FOUNDATIONS
    CONCLUSION
    NOTES

CHAPTER 7: Driving Transformation in Enterprise Environments
7.1: INTRODUCTION
7.2: THE CHALLENGE OF CULTURAL TRANSFORMATION
7.3: TRANSFORMATIONAL LEADERSHIP
7.4: THE KEYS TO A SUCCESSFUL TRANSFORMATION
7.5: TRANSFORMATION CHALLENGES
    CONCLUSION
    NOTES

CHAPTER 8: Measuring DevSecOps
8.1: INTRODUCTION
8.2: KEYS TO A SUCCESSFUL METRICS PROGRAM
8.3: OPERATIONAL METRICS
8.4: BOARD‐LEVEL METRICS
8.5: MEASURING TRANSFORMATION
8.6: CAPABILITY MODELS
    CONCLUSION
    NOTES

CHAPTER 9: Conclusion
9.1: INTRODUCTION
9.2: PEOPLE, PROCESS, AND TECHNOLOGY
9.3: COLLABORATION IS AT THE CORE
9.4: MAKING SECURITY PART OF HOW YOU WORK
9.5: WHERE TO START
9.6: THE FUTURE OF DEVSECOPS
    CONCLUSION
    NOTE


'''

'''
CHAPTER 1: Introducing DevSecOps
'''

'''
1.1: WHY DEVSECOPS? WHY NOW?
'''

'''
-- The meta for technology engineers was to balance the speed of delivery with security and performance.
   THIS HAS CHANGED WITH DEVSECOPS: because we can now deliver at speed without compromising security, privacy or system performance

-- The Goal of DevSecOps: offer the ability to build reliable, secure, and maintainable products without sacrificing speed to market.
-- This is achieved by (moving away from the older approach of gating) shifting responsibilities earlier in the development pipline
   (That means collaboration to integrate security across technical applications/ services. Utilizing automation and education)
'''

'''
1.2: DevOps OVERVIEW
'''

'''
-- REMINDER: The people/process/technology of DevOps advance the way that engineers will build/deploy/manage technical systems.
          -- This is done by: bridging the gap betweem development and operations teams to get products to market quickly while handling
             the nonfunctional requirements like scalability and stability.

-- DevOps are based on Lean principles and Collabration (VS the common thought that it's about technology/ies.)
   -- Commonly thought of as teh intersection of: (Development, Operations, Quality Assurance)             
'''

'''
SUBSECTION: The Three Ways of DevOps
'''

'''
-- The next section is based on the Three ways.

-- The First way: (focuses on the flow through the entire system) 
 - Thinking ReFraming: From, what is my job. To, how do we deliver value to customers.
 
 --The following are examples of the First Way of DevOps:
    1. Shared Goals:
        -ie: having a same direction for a company to go vs a team focusing on new functionality and another on stability
    2. Value Stream Mapping:
        - (Value Stream analysis is a Lean Management technique for analyzing the process for delivering value to the customer)
        - The goal is to identify potential bottlenecks/ inefficiencies.
    3. Test Automation:
        - ITS A KEY ELEMENT: reduces handoffs between development and QA teams
        - It also eliminates potential bottlenecks
        - Allows for testing during the phases vs after the software has been fully built. (so at all phases of software dev lifecycle)

-- The Second Way: (about creating feedback loops):
 - This way focuses on getting input from customers to the people who build the product. (aim for shortening feedback loops)

 --The following are examples of the Second Way of DevOps:
    1. A/B Testing:
        - It's the process of comparing and testing hypotheses about a product's performance in a production environment
    2. Feature Flags:
        - Feature Flags are methods for turning features on and off.
        - This would enable companies to push features to production without additional changes to the code in production
        - (this inturn would allow for companies to push new features to production without affecting timing of marketing launches or other 
           timing of marketing)
    3. Continuous Customer Contact:
        - (One of the best ways to get feedack is to meet directly with customers)
        - It's always critical to hear input at all stages of the product 

-- The Third Way: (focuses on experimentation and learning)
 - (This would mean that it is required to build a learning culture that is always reflecting on mistakes/ learning from them/ 
    and using the learnings to grow and improve )

 --The following are examples of the Third Way of DevOps:
    1. Chaos Engineering:
        - (Chaos Engineering is a practice where reandom errors are intentionally inserted into the system to ensure that the system,
           the processes, and the people are resilient and able to react and respond appropriately.)
        - They can be like the following: software defects, hardware failures, security misconfigurations, etc
    2. 20% of the time:
        - (this refers to reserving 20% of the resources time to do work focused on innovation and experimentation)
        - In this case, about 1 day a week.
    3. Hackathons:
        - (this refers to the practice of designating a set period of time where organizations form teams to do focused work on 
           building innovative new ideas.) (can be weeklong focused efforts on demonstration of the work created)
    4. Blameless Culture and Blameless Postmortems
        - (this refers to providing a safe space to review past incidents without trying to find anyone or any one thing to blame)
        - These are instead focused on using incidents as learning opportunities
'''

'''
SUBSECTION: The Five Ideals
'''

'''
-- From the book: the unicorn project gene kim
-- These are second set of perspective giving characteristics for the team level:
    -The First Ideal: Locality and Simplicity
    -The Second Ideal: Focus, Flow, and Joy
    -The Third Ideal: Improvement of Daily Work
    -The Fourth Ideal: Psychological Safety
    -The Fifth Ideal: Customer Focus

'''

'''
SUBSECTION: The CALMS Framework
'''

'''
-- (This is another approach to devops)
-- CALMS stands for:
    -Culture:      Work together to achieve a goal
    -Automation:   Automation through methods like CD and Infrastructure as code to ensure continuous flow of value to customers.
    -Lean:         (Lean Management Principles: ie, small batches) (made for manufacturing but works here.) (reason for small batches is
                    to reduce inventory, backlogs, work in progress while incrementally delivering value to the customer)
    -Measurement: extraction of key data that provides everyone with constant opportunities to learn/improve
    -Sharing:     refers to the need for open communication/transparency/collaboration at all levels and stages

'''

'''
SUBSECTION: DevOps as an Anti-Pattern
'''

'''
-- DevOps can be seen as an anti-pattern because of its rejection of the idea that operatons and development should be in separate silos
-- They were orignally both payed for different reasons and had different goals. They could also have been under different companies alltogether
'''


'''
SUBSECTION: Agile and DevOps
'''

'''
-- Agile focuses on development and quality assurance working together to deliver incremental value to customers 
 - Where as: devops takes these same concepts and extends them to operations
 - THEY SHARE THAT they both have goals of getting value to customer quicker and rapidly react to changing market demands

'''

'''
SUBSECTION: DevOps and ITSM
'''

'''
-- DEFINE: (ITIL) IT Infrastructure Library. (ITSM) IT Service Management
 - -Main point is that they both are centered around blame free culture and collaboration
'''

'''
1.3: DevSecOps OVERVIEW
'''

'''
-- As per the graphic, DevSecOps is the overlap of development/ operations/ quality assurance/ cyber-sec
'''

'''
1.4: RUGGED DevOps OVERVIEW
'''

'''
-- Rugged DevOps is based on the Rugged software movement which was started by Joshua Corman/ David Rice/ Jeff Williams in 2010
 - It focuses on developing software that is highly available/ secure/ resilient.

-- In 2012 Corman/ Rice/ Williams pushed up a Rugged Handbook. These are the core principles:
    - I am rugged because I refuse to be a source of my vulnerability or weakness
    - I am rugged because I assure my code will support its mission
    - I am rugged because because my code can face tgese challenges and persist in spite of them
    - I am rugged, not because it is easy, but because ot os necessary and i am up for the challange.

'''


'''
1.5:DevSecOps BUSINESS RESULTS
'''

'''
-- Looking at the "why" shows the importance of any sort of transformation. (its important to understand the motivating factor that 
   justify a costly and time consuming undertaking)

-- Data to justify the WHY:
   (From (DORA) "DevOps Research and Assessment team" from google (from 2021). Data was from high performing orgs)
    -High performing devops teams deploy code 973 times more frequently than low performers.
    -Lead time change 6,570x faster than lower performing teams (Time from commit to deploy)
    -The high performers had a decrease of failures vs the lower performers (7.5% vs 23%)
    ^- And when failure did occur, it was restored 6,570x faster than low performing teams

-Keyword meterics: flow time/ lead time, (MTTR) mean time to restore, Employee engagement ****************************************
'''

'''
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________

'''


'''
CHAPTER 2: The Evolution of Cybersecurity (from Perimeter to Zero Trust)
'''

'''
2.1: THE EVOLUTION OF THE THREAT LANDSCAPE
'''
'''
SUBSECTION: Evolution of Infrastructure
'''

'''
-- Traditional Cyversecurity approaches were orignally only focused on securing the edge of the network (perimeter) (only for physical 
   on prem)
-- This changed over time from the on premises model to a cloud based model
-- (based on the Verizon 2022 data breach Investigation Report) - The main ways in which your business is exposed to the internet is the
   same way your business is exposed to the bad guys.

-- The cloud based attack vectors got worse with the rise of hybrid work.
-- It first got worse with BYOD when unsecured/ unmanaged devices where permitted network use.

-- This lead to the simple idea of "A hard outside and a soft inside is no longer viable"

-- Perimeter security is also called castle and moat.

-- This lead to the rise of "Defense in Depth" and "Zero Trust Security" 
'''

'''
SUBSECTION: Evolution of Application Delivery
'''

'''
-- Originally the software that was being sold had to work out of the box because in order to get fixes out, customers would've 
   had to get another cd, go to a website, or they're out of luck. 
-- Where as today, you can use waterfall methodology to make and deliver the product as you go. (including update as you go)
-- This allows for SaaS to rise in use where its all held by the company for customer use
'''

'''
SUBSECTION: The Evolution of the Threat Landscape
'''

'''
-- With time, the attack vector of systems/software has increased tremendously while simultaneously the value of breaches have increased
-- Viruses also went from mainly being harmless jokes to increasing in damage/threat over time.

-- 1988 was the first DOS attack where Robert Tappan of cornell accidentally created the `morris worm`
 - he was later convicted of a felony under the computer fraud and abuse act.
-- THIS LEAD TO: the creation of (CERT) Computer emergency reponse team. (Federally funded reseach center focused on improving the sec
   of software on the internet)
-- Today: APT/organized crimes are the main driver for exposing existential/ global vulnerabilities

-- Lateral Movement: Attacks that include complex movement from the breached system to adjacent systems
-- Supply Chain Attacks: Attacks made at intermediaries to get to the intended targets. (IE: open source products, vendors, products/service)
'''

'''
2.2: THE EVOLUTION OF CYBERSECURITY RESPONSE
'''
'''
SUBSECTION: Defense In Depth
'''

'''
-- Defense in Depth: InfoSec strategy integrating people/tech/ops capabilities to establish variable barriers across multiple layers
   and dimensions of the org
 - It also recognizes that because the perimeter is deterioratiing and/or non existant, it is necessary to have a defense at every layer.
 - If a perimeter exists at all, you must assume the attacker has already breached it and ensure that other attack vectors are protected
   as well
 - In addition, Defense in depth recognises that sec is not limited to the perimeter but rather extends beyond tech to the people involved

-- A layered approach would work like so:
    Data          in the center
    Host          |
    Application   |
    Network       |
    Perimeter     At the edge

-- At each layer, different security measures are then used to protect that layer
   Like the following:

   - Perimeter Security: (phys/tech boundaries)(deadbolt locks, email sec, Intrusion Detection Systems, etc)
   - Network Security: (sec related to networks that an org uses to transmit info) (firewalls/DMZ/VPNS, etc)
   - Application Security: (sec of technical apps/services) (vuln scanners/ software compostion analysis(sca)/ static appsec 
     testing(SAST)/ dynamic appsec testing (DAST), ETC)
   - Data Security: (protection of companies digital info) (identity and access management(IAM)/ data classification/ encryption)

-- DiD includes operational/governance activities by both people and tech

-- Telemetery: measurement of data collected by the tools/ instrumentation designed to measure a systems performance.
 - THe USE OF TELEMETERY: Ops teams can provide 24/7/365 support and response when critical issues arise

-- As per a (SLA) Sevice level agreement, a governance team may be responsible for tracking all vulnerabilities reported from various
   sources and ensuring that they are remediated

'''

'''
SUBSECTION: Defense In Depth
'''

'''
-- `Never Trust, always verify`
-- Zero Trust: a security concept centered on the belief that orgs shouldnt automatically trust anything inside or outside of its
   perimeters. Instead needs to verify anything/everything trying to connect to any system before granting access

-- This is broken into 5 pillars:
    -Identity: Attributes that allow systems to uniquely recognize an entity that is trying to take action. 
        -(Approaches: Least Privilege/ movement to 2fa/ need to continuously validate and not just when granted)
    -Device: Any hardware asset that can connect to a network
        -(Zero Trust maturity model asks for validating the identity of the users and ensuring the security of each device they access)
    -Network/Environment: medium in which digital communications flow (whether wireless/lan/ or internet)
        -(secure net design: Segmentation: (Dividing the network down into smaller segments, based on workload)/ Micro-Segmentation: 
          same as before but even smaller/ encryption/ machine learning based threat protection)
    -Application Workload: Application and services managed by the company corresponding to the application layer in the DiD approach
        -(recommended activities for protection: continuous auth/ behavioral analysis/ integrated Sec testing for pipleline deployment)
    -Data: The companies data assets at rest and transit whether its devices/ storage devices/ databases
        -(Zero trust techniques include: tagging and catagorization for tracking purposes/ encryption/ strict access based controls)

-- Products that are sold as Zero trust solutions are usually misleading and that they use the names zero trust/ DiD but dont work as 
   the concepts suggest. The concepts should be applied hollistically and cannot be solved by any one product/ service

'''

'''
SUBSECTION: Shift Left
'''

''' 
-- Shift left: is the concept of doing tasks earlierin the development process than they are traditionally done
-- By testing earlier in the development process, time and effort to address the issues can be significantly reduced (even to security)

-- Shift left testomg approach takes advantage of the fact that, by doing testing earlier in the development process, the cost of 
   identifying and remediating defects is significantly reduced.

-- Larry Smith introduced the term in sept 2001 in his article of shift left testing. He wrote that `shift left testing is how i refer
   to a better way of integrating the QA and development parts of a software project. By linking these 2 functions at lower levels of
   management, you can expand your testing program while reducing manpower and equipment needs-sometimes by as much as an order of 
   magnitude`

-- By shifting testing earlier in the process, you reduce the time to identify/remediate issues, thus increasing flow of value key to
   Kims first way of devops
-- Shifting testing left helps amplify/shorten feedback loops.

-- By doing security testing closer to when the code is actually being produced/ shorten the amount of time between dev and feedback on
   that work

'''

'''
SUBSECTION: Benefits of Shift Left
'''

''' 
-- It increases speed of feedback to developers and thereby reducing effort required to address those issues
-- This is because the nearer developers are to the code writing with potential vulnerabilities.
-- Those more familiar with the code will be the ones who can correct it the easiest (But, if they have a long time to be noticed of the
   defects, they can lose the context of their work. It can take significantly more effort to correct.)

-- The cost to remediate the issues requires developers who are unfamiliar with the code to go in and determine the cause of the 
   vulnerabilities.
-- This may require significant effort to reverse engineer the systems. ON TOP OF the fact that the age/lack of knowledge about the 
   systems may introduce significant risk to the stability of the system.
-- Therefore, it is better to be able to address/remediate the risks at the time of the development. (it would be less costly/risky)

-- A study by Walter Baziuk in 1995 showed that the cost of repairing a defect in production could be 880 times as expensive as the cost
   of fixing the defect in the requirements phase.
-- A study in 2002 from NIST stated that the cost to fix defects after the product was released was 30x that of the defects found at the
   requirements phase

-- If you take smiths work and apply it to DEVSECOPS process, you produce secure code while reducing the time to do so.
-- testing earlier has significant implications for reducing the cost of developing and delivering secure products

-- Challenges arise with the delay of defect removal in addition to the time to cost and remediate.
 - This means that people will be needed for testing more frequently and remediation may be significantly reduced once products have 
   been completed for extended periods of time
 - Defects found later in the development cycle may also require significant re-architecture/ rework. IN ADDITION, when you look at
   security defects, the longer they are in the product, the longer your company is at risk

-- Ci/Cd means that there is always something that needs to be tested.

-- (Use SCA/ SAST/ DAST tools to inject security into the ci/cd pipeline)

'''

'''
SUBSECTION: Smearing left
'''

''' 
-- Shifting Left is not just taking the same task and doing it earlier, BUT doing it as early as possible

-- Dave Stanke a google engineer coined the phrase `Smearing left`
 - He said this: `Shift left doesnt mean shifting the position of a task within a process flow. It also doesnt imply that no testing is
   done just before a release. It shoukd be seen as spreading the task and its concerns to all stages of the process flow. It about
   continuous involvement and feedback`

-- Which re-affirms, not all security testing must wait until the product is built
'''

'''
SUBSECTION: Shift Right
'''

''' 
-- Shift right focuses on increasing testing further to the right in the development life cycle and testing in production

-- Siaf Gunja of Dynatracec writes: `Shift Right methods ensure that applications running in production can withstand real user load
   while ensuring that applications running in production can withstand real user load and ensuring the same high levels of quality`
 - (To truly test a system and build resiliency. Since it is importent to test in production)

-- Practices like Chaos Testing, (injecting failure conditions into production to ensure that they are resilient to such failures) is
   something you can use. 
 - You can also use:
    -A/B Testing: tests 2 versions of a piece of software at once to see what performs better
    -Canary Testing: release an updated version of the software to a small portion of the user population and see how it performs before
     its release to all users

-- Shift right helps to get additional insight in performance of a system under real world conditions
-- It also allows for a person to exercise instrumentation to ensure that anomalies or anything potentially adverse to the customers
   are identified
'''

'''
SUBSECTION: Shift left For DevSecOps
'''

''' 
-- Shift Left is once of the core concepts of DevSecOps, the concept of security is everyones responsibility. This means that developers
   can have a more active role in security

-- Fundementally, security MUST be everyones responsibility and part of everything we do. NOT AN AFTERTHOUGHT to be tested at the end
   or worse yet, ignored all together.

'''

'''
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________

'''


'''
CHAPTER 3: DevSecOps People
'''
'''
3.1: INTRODUCTION
'''

'''
-- (As an over arching idea: People are difficult to change)

-- (In many cases, the safest thing to do is nothing at all. SO it isnt surprising that security community is change resistance)
 - this explains why there is a large majority which are late/ laggards to new tech
'''


'''
3.2: COLLABORATION AT THE CORE
'''
'''
-- Since you will have you hands in all of the parts of building a product, COLLABORATION is the key underpinning principle.

-- From Security Company Synk wrote: `DevSecOps culture focuses on uniting the normally siloed roles of dev/sec/ops into
   a collaborative shared responsibility paradigm. It seeks to break down barriers of finger pointing/ deflection. Intstead it aimes
   to build empathy/ common goals among various disciplines within the org.`

-- `How do you deliver securely without slowing down delivery? - its collaboration.`
   
'''

'''
3.3: DevSecOps CULTURE
'''
'''
SUBSECTION: Trust
'''
'''
-- Trust is the ultimate goal if you are going to work within an organization
-- DevSecOps requires tighter collaboration between teams and this in turn requires trust

-- Geneology of benefits are so: Build team trust, because better trust leads to better collaboration, and better collaboration leads to
   better business outcomes
-- But do not assume good intent from you teammates.

-- Sid Dekker, a professor of human factors and flight safety and director of research at the school of aviation, Lund University, Sweden,
   wrote about human error extensively in his book: The Field Guide to Understanding Human error.
 - He wrote that the tendency to look for individual blame erodes trust. Which is so essential to building a strong team
 - He wrote `Getting Rid of Bad Apples tends to send a signal to other people to e more careful with what they do/say/report/disclose.
             It does not make human errors go away, but instead seems to make the evidence for them go away; Evidence that might have
             otherwise  have been available to you and your organization so that you could learn and improve`

Some Steps that can be done to increase trust on the team:
    - Create opportunities to meet face to face
    - Be Open and Honest about failure (lack of trust is blame game. High Trust is open comms where stuff went wrong)
    - Be truthful (Also follow through on promises made)
    - Be empathetic (personally understand each individual)

-- Many Studies have found a correlation between intra-team trust and performance.
 - This came from an analysis of 55 different studies on the relationships found that 
   `Team trust was positively correlated with team performance and higher levels of trust in business teams. They are generally associated
    with higher levels of team performance`

'''
'''
SUBSECTION: Transparency
'''
''' 
-- It is important to share data as much as possible without risking of your systems. This applies to transparency of your business plans
   as well as transparency in your data.

-- you obviously cant be transparent about implementation details of your cyber defenses. (can be used to breach you)
-- BUT, transparency is seeing positive results even with cyber security

-- A survey by Deloitte of people who received a breach notification found that 34% said that they trusted organization more.
 - In addition, 73% of this cohort who recieved a privacy breach notification did not trust the org any less following the notification

'''

'''
3.4: THE SHARED RESPONSIBILITY MODEL
'''
'''
-- Since the focus of DecSecOps is on collaboration, there must be a model used of shared responsibilities where everyone is responsible
   for security.
 - EVERYONE, not just the security team
 - The flipside would be that you can't just say `its everyones responsibility now`. That diffusion of responsibilites can lead to a 
   situation where no one takes ownership/ accountability. 

-- This blurring can make it difficult for people to define what is their specific tasks.

'''
'''
SUBSECTION: Ownership
'''
''' 
-- Ownership tends to be a more complex idea than what is given credit. It requires a lot of care/management/completion of a given task

-- One way to address ambiguities is to use a RACI Matrices, that is, RACI matrices detail every task in a given process and define who
   is RESPONSIBLE/ACCOUNTABLE/CONSULTED/INFORMED for each one.
 - this is only to delineate just what ownership means and details all the activities involved in a given process.
 - and it holds accountability

-- the application team must ultimately be accountable for the security and performance of the system.

-- In a 2022 article in Computer weekly, Mandy Andress wrote, `DevSecOps is a mindset and way of working within the application securty
   field in which security is a part of everyones job, not just one team... Orgs should consider delegating responsibility for DevSecOps 
   to engineering teams`

-- In many DevSecOps implementations, the security team may still be accountable for providing the framework/tools/governance for the 
   rest of the org, but dev teams themselves who are accountable for ensuring the sec of the systems they are building

-- by sharing the responsibility for sec, you ensure that you build sec into everything you do, and get sec closer to the source of the
   problem, which leads to more secure products/services

'''

'''
SUBSECTION: Accountability
'''
''' 
-- You must have trust WITH accountability. Especially with a trust based culture, expectations for accountability should be even higher
-- The lack of micromanagement and oversight should be based on the assumption that everyone is responsible for delivering on their 
   promises.

-- If a problem occurs, its very important to be open and honest with the role that person had with the failure
-- THIS MEANS YOU CAN'T HAVE A BLAME ENVIRONMENT!!!
 - This will allow for more honesty around the failures
 - IT WILL ALSO LEAD TO FAILURES BECOMING LEARNING LESSONS

-- Employee engagement surveys and management 360s are useful in understanding the cultural environment
 - That said, the very fact that people are hesitant to share information openly about their failures may be indicative of culture of 
   fear

-- note: some companies still see security as a cost that needs to get paid without real understanding of criticality 

-- Data breaches will effect everyone:
 - 2013 data breach of target lead to its ceo losing his job
 - 2014 breach of sony led to the resignation of the board co-chairman amy pascal

-- A shared responsibility model can be also fostered by building shared goals for the org
 - goals should include sec att the highest levels of the org and these goals should cascade down throughout the org

'''

'''
SUBSECTION: The role of the security team
'''
''' 
-- With DevSecOps, the sec team is no longer a policing org responsible for ensuring that everyone is following the rules and punishing 
   rule breakers. Instead the role of the sec team must shift to gov and guidance

-- The modern sec team shoudl focus on developing the standards and governance around sec and designing systems to automatically 
   monitor/measure/enforce the rules

-- Sec teams are now partners to development/ ops/ SRE teams, helping them to drive the best practices and deliver secure products 

'''

'''
3.5: PSYCHOLOGICAL SAFETY
'''
'''
-- People must have psychological safety

-- The concept first emerged in 1965 in the book Personal and Organizational Change Through Group Methods: The Laboratory Approach
   by Edgar Schein and Warren Bennis. They talk about `an atmosphere where one can take chances ( which experimentalism implies) without
   fear and with sufficent protection`

-- Harvard Business school professor Dr Amy C Edmonson went further with the concept, describing it as `a belief that one will not be
   punished or humilated for speaking up with ideas/ questions/ concerns/ mistakes'

-- Psychological safety is the fourth ideal identified in Gene Kims Book The unicorn project. Kim says `No on will take risks, experiment
   or innovate in a culture of fear, where people are afraid to tell the boss bad news`
 - When people are focused overly on mistake prevention rather than value creation, they often do the minimal work needed. Reducing 
   output for the company

-- From a TedX talk called `Building a Psychologically safe workspace` by Amy Edmonson, she suggested 3 things for fostering good 
   culture for psychological safety:
   1. Frame the work as a learning problem, not an execution problem
   2. Acknowledge your own fallibility
   3. Model Curiosity

-- MAKE THEM FEEL EMPOWERED AND LIKE THEY CAN LEARN
   
'''

'''
SUBSECTION: Empowerment
'''
''' 
-- Engineers are by and large highly educated and highly compensated professions. it is safe to assume that these people ARE doing their
   best work. If you start by trusting that people are trying their best, it helps you to empower them.
 - Manage people around this idea.

-- Instead of managing engineers such as assembly line workers, it is important to approach them like doctors/lawyers.
-- Understanding the immense knowledge they have and empowering them to act independently based on that knowledge

-- When leaders micromanage employees or are quick to blame them for error, those employees tend to do less work than they might 
   otherwise. Examining every piece of work and being quick to criticize creates a culture of fear where people do not strive to do 
   their best but, instead, try only not to make mistakes.

-- In response to employers forcing employees to return to work: forcing them to come back tells them `We do not trust you to do your
   jobs unless we are watching you to do your work.`
 - This begs the question why companies hire people for large sums of money if they can't trust them to do their jos independantly?
 - Either they have hired the wrong people, or they have not built culture that inspires people to do their best.

-- The end goal about highly skilled workforces is delivery

-- Setting values for human contact/ creating events that require in office bonding needs to be a part of how employees work
 - WHILE letting employees know they are trusted and choose when and where to work goes a long way to empower

'''   

'''
SUBSECTION: Learning Culture
'''
''' 
-- Learning culture is open to continually learning

-- You can build a learning culture in daily life using these activities
   - Incident Post Mortems: review an incident after it has been resolved
   - Tabletop Exercises: Walk through theoretical cybersec incidents and discuss parties actions in response
   - Game days: simulate cyber sec event such as an attack or breach to practice the teams response and learn and improve
   - Phising Campaigns: they are tools for sending phising emails to a company's employees to test the ability to identify and respond
   - Training: Use trainings to continuously increase sec knowledge throught the org. The training required should be based on the role 
   - Cross Training: Training that are outside of their own area

-- Part of learning culture is embracing failure as a learning opportunity
-- In The Unicorn Project, Gene kims says: `The corrosive effects that a culture of fear creates, where mistakes are routinely punished
   and scapegoats are fired. Punishing failures and shooting the messenger only cause people to hide their mistakes, and eventually, all
   desire to innovate is completely extinguished`

-- The most successful engineers are the ones that make the most mistakes. (This is because they are working on the hardest tasks,
   driving innovation, and taking risks)

-- It is important to look at the system as a whole and search for opportunites to improve in all areas when looking for errors/mistakes.

-- It important to not seek out individuals responsible and to punish but rather understand all of the elements that contributed to the
   failure

-- When a mistake happens, The org must learn.

'''

'''
SUBSECTION: Security Training programs
''' 
''' 
-- Training should be catered to the people who are responsible for the training

-- The first step in making a good cybersecurity plan is to asses the key threats to the organization as compliance requirements

-- Training Programs can include: new hire training, annual complience training for any in scope complience requirements like (PCI)
   Payment Card Industry for those companies accepting credit cards or (SOX) Sarbanes-Oxley for companies in the public domain, and 
   ongoing knowledge tests such as phishing tests.

--Specific groups of users may require specialized or additional training, such as executives who may be at a heightend risk because
  of their elevated position within the company

-- Based on the 2022 Verizon Data Breach Investigation Report, phising is the 2nd highest risk entry path to exploiting a companies
   environment
-- By Running phising tests and tests of all kinds, you can ensure that there is a constant awareness of the security threats present in
   email

-- Its important to develop training that is interactive and engaging. To that end, make sure that the training is relevant to the 
   audience you are targeting

'''

'''
3.6: ORGANIZING FOR DevSecOps
'''
'''
-- There is no right/ best way to organize DevSecOps
-- If collaboration is built into your culture, many different organizational structures can help build om that collaboration.
 - The reverse is true also, if a culture of collaboration is not there, organizational structure alone will not fix that.

-- `DevOps Topologies` by Matthew Skelton and Manuel Pais discussed many of the diff org patterns and anti-patterns for devOps in which
   they state, `the DevOps topologies reflect 2 key ideas: 
   (1) There is no 1 size fits all approach to structuring teams for DevOps success. The suitability and effectiveness of any given 
       topology depends on the organizations context. 
   (2) There are several topologies known to be deterimental (antipatterns) to devOps success, as they overlok or go against core tenets
       of devops`

-- Skelton and Pais go on to say that `Orgs must design teams intentionally by asking these questions:
   -Given our skills/ constraints/ culture/ engineering maturity/ desired software architecture/ and business goals/ which team topology
   will help us deliver results faster and safer?
   -How can we reduce/ avoid handovers between teams in the main flow of change?
   -Where should the boundaries be in the software system in order to preserve system viability and encourage rapid flow?
   -How can our teams align that?`

-- The anti-patterns or organizational patterns that deter collaboration may be more impactful

-- The devOps handbook, Gene, Humble, Debois, and Willis write `When infosec is organized as a silo outside of development and operations,
   many problems arise`

-- The reality is that any tech team small enough to be fully self-contained is, by its nature, doing DecSecOps insomuch as they are working
   together to do all the parts of the product development/ sec/ ops.
 - It is only at scale tha tyou really start to see specialization working in. Which in turn, needs to be broken down.

-- The concept of site reliability engineering originated at google in 2003 with the idea that teams needed a role to focus efforts on
   the reliability of the system.

-- Google, there is a core site reliability engineering team, which provides guidance/ gov/ frameworks/ standards/ shared tooling.
   In addition, there is another part of the team of SREs embedded within other teams.

-- Embedded Site reliability engineers focus on a deep understanding of reliability engineering as it applies to the specific product 
   or service of the team in which they are working

-- With this model, a core team provides sec standards and direction to other groups looking for help.
 - In addition, sec engis/ sec champoins are embedded w/in the app teams.

'''

'''
3.7: BUILDING A DevSecOps CULTURE
'''
'''
SUBSECTION: Security Champions
''' 
'''
-- Security Champions program empowers SREs/ Dev/ and quality engineers to become champions of their teams. This person can help bridge
   the gap by evangelizing/ managing/ enforcing the security posture while acting as an exteneded member of the sec tweam.

-- Sec Champions should be Voluntary and be people who desire to learn more cybersec
 - They become a point of contact for sec-related questions/ concerns w/in their respective application team.
 - They provide an opportunity for people who are interested in sec to learn valuable new skills.
 - In addition, sec champs build valuable cross-team and cross-org relationships which inc their value to the company while building 
   DevSecOps culture.

-- Sec Champs can form a group that spans the comany to enable continues learning and best practices sharing. Reg Sec Champ meetings
   help build collab and continual learning throughout the company.
 - Sec Champs programs also func as a way to drive standards and best practices across the org.

-- Sec Champs help embed sec into every team. This in turn emphasizes the idea that sec is everyones responsibility and not just domain
   of separate sec team.

'''
'''
SUBSECTION: Internal Bug Bounties
''' 
''' 
-- These programs offer a reward for anyone who can identify sec vulns in existing products.
 - They help build sec awareness while helping ensure the sec of the products. 
 - (incentives can come in the form of recognition or even monetary comp)

 -- Not only do sec-related bug bounties help identify potential sec issues w/in the companys product, but they also encourage employees
    to better understand the avenues an adversay might exploit and therefore become more knowledgable about pitfalls to be avoided.

'''

'''
3.8: THE EVOLUTION OF THE EMPLOYEE (T‐SHAPED PEOPLE)
'''
'''
-- As people must understand not only their individual domains but also the broader technical enviroment in which they are operating.
 - in addition, they must understand the broader business context within which they are operating.

-- Developers must not only understand the programming language in which they are developing, they must have the breadth of knowledge
   extending to the infrastructure they are operating on as well as the security requirements for their application

-- Expanding the breadth of developers knowledge to security/infrastructure is aided by abstraction/ automation of these elements.
 - ie: using AWS means that developers do not know the details of router configuration, but they must, still understand how to implement
   their services via AWS services

-- You cannot expect every engineer to also be a sec engineer, but you can expect them to be sec conscious.
 - By doing things like automating deployment of end point sec (and embedding it into AWS image in this case), you provide the automation
   to easily enable sec best practices and enable T-shaped employees to succeed.

-- However, it does mean that every engineer needs to be aware of broad spectrum of operational/ sec requirements in which their systems
   are going to operate, they must be able capable of building their systems and ensuring they continue to run in a secure way.

'''

'''
3.9: HIRING FOR DevSecOps
'''
'''
-- Hiring for DevSecOps engineeers means finding people who are not only good technically, but more importantly, who are good collaborators
 - A very importent characteristic of a good engineer will be the soft skills

-- Those key characteristics include:
   -Creative problem solving
   -Communication
   -Collaboration
   -Curiosity

The following questions would be able to illuminate practical teamwork skills:
   - Tell me a time when your team had a conflict and what you did to resolve it
   - Tell me about a time when you had a conflict with you supervisor and what you did to resolve it
   - Tell me about a time a project you were working on was not going in the right direction and what you did to resolve it

-- If a comoany has long delays in the hiring process or is not well organized, you can miss on the best talent.

'''
'''
--End of chapter note:
   -Trust breeds empowerment
   -Trust encourage transparency
   -Trust with Transparency enables a learning culture.
'''

'''
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________

'''

'''
CHAPTER 4: DevSecOps Process
'''
'''
4.1: INTRODUCTION
'''
'''
-- Fundamentally, DevSecOps proccesses are:
   - Lightweight
   - Automated
   - Trustful
   - Measured
   - Driving Ownership and accountability
   - Transparent
   - Empowering
   - Engendering of psychological safety
   - Focused on developing a learning culture

'''
'''
4.2: UNDERSTANDING PROCESSES AT SCALE
'''
'''
-- When an enterprise is moving faster, they need to have the process framework in place to ensure smooth/ consistent execution

-- As companies grow, it becomes imperative that they have the process to track activities and react when problems arise

-- when companies are performing tens/ hundereds of release a day, they need to have a record of releases. So when something breaks, 
   they can easily find what changed and quickly fix it.
-- For midsize/ large companies, you need to know what is changing/ what the process is/ who needs to get involved to engage the right
   people and respond quickly to get services restored during major incidents.

''' 

'''
4.3: DevSecOps FOR IT SERVICE MANAGEMENT
'''
'''
--(ITSM) IT Service Management is the processes a company uses to manage its tech products/services.
 - (ITIL) Info Tech Infrastructure Library is a framework for ITSM. It provides a process framework for the management of tech and
   alignment with delivery of value to the customer.
 - ITIL includes processes such as Incident Management/ Problem Management/ Change Management
 - ITIL is a framework from which you can take/leave portions you like, it provides many useful processes for DevOps.

-- Integrating process frameworks such as ITIL w/ DevSecOps Principles becomes increasingly critical at scale:
   - Incident management: When you have millions of moving pieces and hundreds of gloablly distributed teams, it is significantly more
                          important that you have a framework for responding appropriately when something goes wrong.
                          At a small scale everyone knows who wrote the code. It may even be the same engineer who set up the server
                          the code runs on. (means diag/ responding requires lower coordination.)
   - Problems management: Focuses on understanding and remediating the root cause of incidents.
                          The best practice here is to not just be reacting when incidents occur, but instead be proactive and making
                          sure that they dont occur in the first place
   - Change managment: Enables rapid releases/ encourage devops practices/ improve stability

-- One way to do this the above is by taking an adaptive approach to change management. To balance the risk with business agility.
 - That approach can account for the level of automation/ resilience built into the software/ release process to allow for rapid 
   releases while automatically tracking all changes in the system.


'''

'''
4.4: SECURITY INCIDENT MANAGEMENT
'''
'''
-- Service Management process of incident management is focused on the resolution of issues impacting tech services
 - Tools such as enterprise chat/ notification systems can help ensure that the right people are engaged at the right team.

-- DevSecOps focuses a lot on system telemetry, which is the data you collect about how your systems and services are performing.
 - If you can instrument your systems properly, you can find issues before they imoact customers and prevent minor incidents from
   becoming major incidents.
 - In addition, if systems are properly instrumented, you can begin to apply machine learning/ predictive analysis to anticipate 
   incidents before they happen

-- DevOps has a its roots in Lean manufacturing.
 - One of the processes that was borrowed from lean was the andon cord. The cord is used to shut down an assembly line when something
   goes wrong
 - You can apply a similar concept to incident management by allowing anyone to declare an incident when there is a system error
 - With that, you can bring all resources to bear on an issue w/ the concept called swarming

-- Full Stack engineers focus on the system as a whole rather than individual vertical slices, while functional teams focus on isolated
   functionality, which can be developed w/o dependence on other teams.
 - This leads to engineers can take full responsibility for resolving issues w/in their domains rather than needing to `throw them over
   the wall` to another team that might have shared responsibility

-- For modern devops, maintaining the state is no longer important, so incident responders can easily restart the systems on which 
   applications run. (in some cases, you can kill the whole app/service)

-- For services with short lived/non existent infrastructure, the resolution process changes from investigate and diagnose to rapid 
   restart/ restore procedures, leading to significant improvments to resolution times.
 - You still can't ignore the diagnosis, but it's important to capture important info such as application/ system logs so that diagnosis
   can happen at a later time.
 - Without further investigation or post incident reviews, you cannot build a learning culture nor can you prevent repeat incidents from
   occuring
'''
'''
4.5: CHANGE MANAGEMENT
'''
'''
-- Change management is the IT serviec management process of focusing on managing changes to the technical environment to ensure that 
   the new changes are successfully made while minimizing negative impact. Change management can be particularly important for security
   as appropriate change management can help enusre that changes adhere to an orgs sec policies

-- The Implemenetation usually goes against the way devops works because change management requires layers of approval for every change
   and inserting significant slow downs and almost guaranteeing longer release cycles and delays in getting value to the customer
 - (DevOps fundamentals focuses on short release cycles and rapid delivery of value to customers)

-- Tracking changes in technical environment can be highly valuable.
 - This is especially true for large environments with small batch deployment where many diff changes are occuring at the same time.
   It is critical to have visibility into what is changing and how those changes might impact one another and the end customer

-- Instead of using change  management as a gate to prevent change, use it as a process to enable change to get to your customers quickly
   and securely

-- The DevOps approach to change management is that you shift the focus from that nearsighted focus of security/stability to the broader
   perspective that change management itself enables security/ agility while ensuring stability

-- To do change management at a pace of hundreds a day, you must automate your change management process
 - ITSM workflow tools like service now expose APIs which define and allow for other apps to interface with them on a programmatic basis

'''

'''
SUBSECTION: Adaptive change management
''' 
''' 
-- The goal of adaptive change management is to implement lightweight/ scalable/ agile processes to improve stability while keeping 
   a high pace of delivery velocity
-- This process takes into account risk of a change, which leads to ensuring that appropriate amount of attention is paid to high risk
   changes without slowing down low risk changes

-- In this approach of change management, every change is assigned a risk based on a risk calculation by the team implementing the change
-- Approval and oversight levels are then dynamically adjusted based on the risk of given change. In addition, release times can be 
   adjusted in accordance with risk levels

-- CI/CD and deploying small updates to a small subset of users (A/B testing) lower the risk of a given change. With adaptive change
   management, low risk changes with w/fully automated CI/CD and A/B deployments are released w/o any approvals. 

'''
'''
SUBSECTION: Change Risk Calculation
''' 
''' 
-- Risk calculation can have its probability to reflect the likelihood that a given risk will occur, while impact reflects the impact 
   on the business if a risk occurs regardless of the propbability.

-- For trust, it is important to allow your team to assess their own risk.
'''
'''
SUBSECTION: Guiding principles for change review and approval
''' 
''' 
-- Low-Risk changes may require review from managers.
 - High Risk changes may require coordnation w/other teams when there are cross dependencies and sometimes may benefit from a review by
   a change advisory board (CAB)

-- When aligning approval witg risk, keep in mind the following:
   - The closer the change reviewer is to the technical details of the code, the better. (they will have a much better idea of the 
     impact that the code change will have.)
   - While high trust is critical, an audit should require that there be another set of eyes reviewing changes to prevent people from
     making illicit or damaging changes when they have malicious intent
   - The CAB, if one is needed, should act as flight control, coordinating between different teams and business needs. (NOT a bureaucratic
     body designed to stop changes)
   - Small incremental changes are safer.
   - the easier you make it to submit a change, the more likely people are to follow the process
'''

'''
SUBSECTION: Standard Changes and change freezes
''' 
''' 
-- There are also standard changes that do not require approval. This is the ideal state for changes in a DevSecOps world.

-- Standard changes are pre-approved changes that are extremely low risk, relatively common and follow a set process.
 - With that, you can automate deployment with ci/cd, which includes  best practices like continuous testing/ automated rollbacl/ feature
   flags and the like.

-- For the change to qualify as a standar change, it must be a low risk and have a history of successful performance.
 - Once approved, these standard changes can be deployed w/o any approval other than code review. (this is ideal for an org that wants
   to move quickly)

-- note: The evidence indicates that change freezes do not work.
 - Change freezes are common practice in many businesses where, during critical business periods no changes are allowed.
 - There are many reasons why this doesnt work:
   - First of which is that even during high risk times business/ tech must continue to move forward. 
   - With that, there are almost always exceptions to change freezes. (they are called change slushies.)

-- change freezes often cause a huge influx of changes directly before the freeze. (So, teams will cram in all their critical features
   directly before a high risk, leading to significant instability during the period of time that the business is trying to protect)
 - On top of that, there will be a flood of releases DIRECTLY after the change period.

-- Another problem w/ change freeze periods is that they treat low risk changes the same way they treat high-risk changes.
 - (A way to adaptively approach it is that we could just raise all of the risks of any of the changes)

-- Emphasis: ALL TESTING, from unity level to integration to vulnerability testing. The key is to automate wherever possible and to 
   build this automation into your dev pipeline

-- Balance to maintain: time perspective. Tests need to test full system functionality and also be fast if they are going to be used in
   in a rapidly deploying pipeline.
-- The reason you want the tests to be fast is so that the developers wouldnt be tempted to skip testing or do less frequent releases
 - It is ultimately up to the responsibility of the team developing the code to determine the balance

-- To accomodate rapid change, it is often important to allow verbal approval for emergancy circumstances. It is often also appropriate
   to delay the filings of any change forms until after the emergancy situation has been remediated.

'''

'''
4.6: PROBLEM MANAGEMENT
'''
'''
-- Problem management looks at and attempts to address, the underlying causes of incidents

-- `The primary objectives of this ITIL process are to prevent incidents from happening, and to minimize the impact of incidents that
   cannot be prevented.`

-- The first step in the problem management process is the identificationof the problem. 
-- IMPORTANT: problem management should not be reserved only for major incidents.
 - (often it is only the minor incidents that are the most insidious because it is the risk of the death by 1000 paper cuts.) where as
   enough small problems build up to a big one that takes down the systems.
-- This approach may incur additional cost of availablity managers, but the cost outweighs the detreimental impact of ouatages/ performance
   degradation

-- (PIR) post incident review/ incident postmordem: the first step of problem management/ and an excellent opportunity to insitll 
   insitutional learning for an org. (during this, the underlying cause may be determined/ or a temp fix applied)
'''

'''
SUBSECTION: The Problem Manager Role
''' 
''' 
-- More commonly, companies use incident managers as dual roles with problem managers.
 - (issue with that is that this will decrease the effort/ energy that would go to problem resolution)
 - if incident managers are taking too much time fighting fires, they cannot build a better mode of fighting them.

-- (important to have someone whose job it is to identify and drive the resolution of problems)
'''
'''
SUBSECTION: Blameless postmortems
''' 
''' 
-- Blameless postmortems very good for learning and rather than blame.
-- Key goal of post mortems: (not to just solve a problem/ find a root cause, but to ensure the org gets a learning experience)

-- If everyone leacing the postmortem has learned something, then the postmortem should be considered a success even if no other action
   is taken

-- From The Unicorn Project, at the beginning of the post mortems meetings, one of the qa managers states `The spirit and intent of these
   sessions are to learn from them, chronicling what happend before the memory fades. Prevention requires honesty, and honesty requires
   the absence of fear.`

-- From Etsys Code as Craft blog post, `blameless postmortems and a just culture, a funny thing happens when engineers make mistakes and
   feel safe about it. They are not only willing to be held accountable, they are also enthusiastic in helping the rest of the company
   avoid the same error in the future.`

'''

'''
4.7: RELEASE MANAGEMENT
'''
'''
-- (A deployment tools such as Jenkins can be used CI/CD in a fully automated manner.)
 - These tools enables the small incremental releases which is, at the core of DevOps.
 - These tools allow for rapid deployment of software/ infrastructure that can enable automated testing and sec scanning

-- By adding sec tooling into the deployment pipeline, you can ensure that all releases follow org sec standards.
'''

'''
4.8: A DevOps APPROACH TO SECURITY PROCESSES
'''
'''
SUBSECTION: Table top exercises
''' 
''' 
-- A tatble tops is simulate a cyber attack and cross functional team responses.
-- Benefits of table tops:
   - Increased awareness of threats across teams within a business
   - Opportunities to eval incident preparedness
   - Find gaps in IR plan
   - Clarify the roles/ responsibilites as well as decision making
   - Identify possible capability gaps

'''
'''
SUBSECTION: Attack Simulation: Red Team, Blue Team, Purple Team
''' 
'''
-- Attack simulation: groups either attack or defend an almost live system (the goal is to breach sec)
 - Usually using hands on systems.
 - Make the process regular and repeated
 - (IE: find a regular cadence to repeat these events)

'''

'''
4.9: CHAOS ENGINEERING
'''
'''
-- Helps build sys resilience by intentionally injecting errors, (ie: server shutdowns/ latency incrs/ resource exhaustion), into the system
-- (Casey Rosenthal) built Chaos engineering team at Netflix. It is defined as: 'the discipline of experimenting on a distributed system in order to build confidence
   in the systems capability to withstand turbulent conditions in production.'

-- 'With any highly complex system, failure is inevitable, so you need to prepare for failure rather than just try to prevent it.'
-- Not only will systems fail, but as they become more complex, there will be more components to fail/ more opportunities for failure.

-- Chaos Testing is importent because it allows you to learn while not in the middle of an incident.

-- testers should begin with a hypothesis and then develop an automated way of testing that hypothesis.

-- Other failures scenarios might include: catching AWS instances deployed with default perms/ introducing code or infrastructure with critcal vulnerabilites that should
   be caught/ blocked.
'''
'''
CHAPTER 5: DevSecOps Technology
'''
'''
5.1: INTRODUCTION
'''
'''
-- When thinking of if a tool is a 'DevSecOps', it should be be following 'DevSecOps Principles'. Such as:
   -Collaboration: 
   -Flow of value from left to right: CI/CD tools such as `jenkins` and `circleCI` are the key to Gene kims first way of DevOps. (value more for the customers)
   -Empowerment: 
   -Fast Feedback and Continuous Learning: 
   -Shift Left: 

'''

'''
SUBSECTION: DevSecOps CI/CD
''' 
''' 
-- CI/CD is the cornerstone of of DevOps Principles
-- The CI/CD process includes all the steps to take changes to code from the developer and get them built deployed to the customer. They are:
   1. Pushing code from source code repository
   2. Integrating it into the rest of the application
   3. Building a complete application
   4. Testing the application
   5. Deploying the app to prod all through automation

-- It should be noted that CD does not mean that apps are always deployed to customer. Only that the application is always in a deployable state.

-- Tools for each Section of the pipeline:
   1. Commit
      -SAST (static application security testing)
         -SonarQube
         -Veracode
         -Mend
         -Checkmarx
         -Snyk

   2. Build
      -SCA (Source Composition Analysis)
         -Github
         -Gitlab
         -Snyk
         -FOSSA

      -IaC Scanning (Infrastructure as Code)
         -TFLint
         -Gitlab
         -Snyk

   3. Test
      -SAST (static application security testing)
         -SonarQube
         -Veracode
         -Mend
         -CheckMarx
         -Synk

      -DAST (Dynamic application security testing)
         -Checkmarx
         -Rapid 7
         -HCL appscan
      
      -IAST (Interactive application security testing)
         -Contrast Security
         -Invicti
         -Checkmarx
         -Veracode
         

   4. Deploy
      -DAST (Dynamic application security testing)
         -Checkmarx
         -Rapid7
         -HCL appscan

      -RASP (Runtime Application Self Protection)
         -Dynatrace
         -Signal Science
         -JSDefender
         -Imperva
         -OpenRASP
         -Veracode
         -Rapid7

'''
'''
SUBSECTION: The commit stage 
''' 
''' 
--

'''


'''
SUBSECTION: 
''' 
''' 
--

'''









