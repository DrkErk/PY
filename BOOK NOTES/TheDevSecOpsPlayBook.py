
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
-- 

'''


'''
1.3: DevSecOps OVERVIEW
'''

'''

'''


'''
1.4: RUGGED DevOps OVERVIEW
'''

'''

'''


'''
1.5:DevSecOps BUSINESS RESULTS
'''

'''

'''






