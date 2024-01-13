
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
--


'''

'''
3.3: DevSecOps CULTURE
'''
'''
3.4: THE SHARED RESPONSIBILITY MODEL
'''
'''
3.5: PSYCHOLOGICAL SAFETY
'''
'''
3.6: ORGANIZING FOR DevSecOps
'''
'''
3.7: BUILDING A DevSecOps CULTURE
'''
'''
3.8: THE EVOLUTION OF THE EMPLOYEE (T‐SHAPED PEOPLE)
'''
'''
3.9: HIRING FOR DevSecOps
'''













