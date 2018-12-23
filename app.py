# coding=utf-8
from flask import Flask, render_template
import random

app = Flask(__name__)

answers = ["D",
           "A",
           "D",
           "B",
           "C",
           "B",
           "D",
           "C",
           "A",
           "D",
           "C",
           "C",
           "D",
           "C",
           "C",
           "D",
           "C",
           "A",
           "D",
           "D",
           "D",
           "B",
           "A",
           "D",
           "C",
           "B",
           "D",
           "B",
           "A",
           "A",
           "D",
           "A",
           "C",
           "D",
           "B",
           "D",
           "D",
           "B",
           "C",
           "A",
           "D",
           "A",
           "D",
           "C",
           "D",
           "B",
           "A",
           "C",
           "D",
           "B",
           "C",
           "D",
           "D",
           "C",
           "B",
           "A",
           "C",
           "D",
           "D",
           "A",
           "A",
           "C",
           "D",
           "C",
           "D",
           "C",
           "A",
           "C",
           "D",
           "B",
           "D",
           "A",
           "C",
           "B",
           "B",
           "A",
           "D",
           "A",
           "B",
           "B",
           "D",
           "A",
           "D",
           "D",
           "C",
           "D",
           "C",
           "B",
           "A",
           "C",
           "C",
           "C",
           "B",
           "D",
           "D",
           "D",
           "D",
           "C",
           "A",
           "A",
           "B",
           "C",
           "A",
           "A",
           "B",
           "B",
           "A",
           "D",
           "D",
           "D",
           "D",
           "D",
           "B",
           "A",
           "B",
           "C",
           "D",
           "A",
           "B",
           "A",
           "C",
           "B",
           "D",
           "D",
           "B",
           "A",
           "B",
           "C",
           "B",
           "C",
           "A",
           "B",
           "C",
           "A",
           "A",
           "A",
           "C",
           "D",
           "A",
           "A",
           "A",
           "B",
           "D",
           "A",
           "B",
           "D",
           "D",
           "C",
           "C",
           "A",
           "A",
           "D",
           "B",
           "C",
           "C",
           "A",
           "D",
           "B",
           "B",
           "C",
           "D",
           "A",
           "D",
           "D",
           "B",
           "D",
           "A",
           "C",
           "A",
           "B",
           "D",
           "D",
           "D",
           "C",
           "C",
           "A",
           "A",
           "C",
           "D",
           "C",
           "A",
           "C",
           "A",
           "C",
           "D",
           "C",
           "A",
           "D",
           "A",
           "C",
           "B",
           "D",
           "B",
           "B",
           "A",
           "D",
           "C",
           "A",
           "B",
           "A",
           "B",
           "D",
           "A",
           "A",
           "C",
           "D",
           "D",
           "C",
           "C",
           "C",
           "C",
           "C",
           "B",
           "D",
           "B",
           "C",
           "C",
           "A",
           "A",
           "D",
           "D",
           "A",
           "A",
           "C",
           "A",
           "B",
           "A",
           "D",
           "A",
           "A",
           "C",
           "D",
           "D",
           "D",
           "B",
           "C",
           "D",
           "A",
           "C",
           "A",
           "D",
           "C",
           "D",
           "A",
           "C",
           "C",
           "D",
           "D",
           "A",
           "D",
           "B",
           "C",
           "A",
           "D",
           "B",
           "C",
           "A",
           "B",
           "C",
           "A",
           "B",
           "C",
           "D",
           "B",
           "A",
           "C",
           "A",
           "B",
           "D",
           "C",
           "A",
           "D",
           "C",
           "B",
           "C",
           "B",
           "A",
           "B",
           "D",
           "A",
           "C",
           "D",
           "A",
           "B",
           "C",
           "D",
           "D",
           "A",
           "C",
           "C",
           "B",
           "A",
           "B",
           "A",
           "D",
           "C",
           "D",
           "D",
           "B",
           "A",
           "B",
           "B",
           "C",
           "D",
           "C",
           "A",
           "B",
           "B",
           "A",
           "C",
           "C",
           "D",
           "C",
           "B",
           "D",
           "C",
           "A",
           "D",
           "C",
           "B",
           "A",
           "C",
           "D",
           "D",
           "B",
           "C",
           "A",
           "A",
           "D",
           "D",
           "A",
           "A",
           "B",
           "D",
           "B",
           "D",
           "C",
           "D",
           "C",
           "B",
           "D",
           "C",
           "A",
           "A",
           "A",
           "B",
           "B",
           "B",
           "B",
           "C",
           "B",
           "B",
           "D",
           "D",
           "D",
           "B",
           "C",
           "D",
           "A",
           "C",
           "D",
           "C",
           "A",
           "C",
           "B",
           "B",
           "A",
           "C",
           "C",
           "D",
           "B",
           "A",
           "B",
           "A",
           "D",
           "C",
           "C",
           "C",
           "A",
           "B",
           "C",
           "D",
           "D",
           "A",
           "C",
           "C",
           "D",
           "B",
           "B",
           "C",
           "D",
           "D",
           "D",
           "D",
           "B",
           "C",
           "D",
           "A",
           "C",
           "B",
           "A",
           "B",
           "C",
           "A",
           "D",
           "C",
           "C",
           "A",
           "D",
           "A",
           "B",
           "D",
           "C",
           "B",
           "C",
           "C",
           "B",
           "D",
           "D",
           "C",
           "C",
           "B",
           "B",
           "D",
           "C",
           "A",
           "B",
           "A",
           "C",
           "A",
           "B",
           "C",
           "C",
           "D",
           "D",
           "B",
           "D",
           "D",
           "A",
           "C",
           "A",
           "D",
           "B",
           "A",
           "D",
           "C",
           "C",
           "A",
           "C",
           "B",
           "C",
           "B",
           "D",
           "C",
           "A",
           "B",
           "D",
           "A",
           "A",
           "B",
           "D",
           "D",
           "B",
           "A",
           "C",
           "D",
           "B",
           "B",
           "A",
           "D",
           "C",
           "D",
           "A",
           "C",
           "D",
           "C",
           "D",
           "A",
           "D",
           "A",
           "A",
           "B",
           "B",
           "D",
           "C",
           "D",
           "A",
           "A",
           "D",
           "D",
           "B",
           "A",
           "B",
           "C",
           "B",
           "A",
           "A",
           "B",
           "D",
           "A",
           "A",
           "D",
           "D",
           "B",
           "D",
           "C",
           "A",
           "D",
           "D",
           "D",
           "D",
           "D",
           "A",
           "A",
           "D",
           "C",
           "B",
           "C",
           "D",
           "D",
           "B",
           "D",
           "C",
           "C",
           "B",
           "A",
           "C",
           "D",
           "B",
           "D",
           "B",
           "A",
           "C",
           "D",
           "B",
           "D",
           "B",
           "D",
           "A",
           "C",
           "D",
           "B",
           "D",
           "D",
           "D",
           "A",
           "C",
           "D",
           "B",
           "B",
           "B",
           "B",
           "C",
           "D",
           "D",
           "B",
           "A",
           "B",
           "C",
           "A",
           "B",
           "C",
           "B",
           "C",
           "C",
           "B",
           "B",
           "A",
           "A",
           "C",
           "D",
           "D",
           "C",
           "D",
           "A",
           "B",
           "D",
           "B",
           "A",
           "A",
           "B",
           "D",
           "C",
           "C",
           "D",
           "B",
           "D",
           "D",
           "C",
           "A",
           "B",
           "C",
           "B",
           "D",
           "D",
           "A",
           "D",
           "B",
           "C",
           "B",
           "A",
           "A",
           "B",
           "C",
           "D",
           "B",
           "B",
           "C",
           "A",
           "B",
           "D",
           "C",
           "A",
           "D",
           "B",
           "B",
           "A",
           "B",
           "D",
           "C",
           "B",
           "A",
           "C",
           "C",
           "B",
           "B",
           "B",
           "B",
           "D",
           "D",
           "C",
           "B",
           "A",
           "A",
           "C",
           "A",
           "B",
           "C",
           "D",
           "D",
           "A",
           "B",
           "D",
           "B",
           "A",
           "C",
           "C",
           "B",
           "D",
           "A",
           "C",
           "D",
           "A",
           "B",
           "D",
           "C",
           "A",
           "D",
           "B",
           "B",
           "D",
           "C",
           "B",
           "A",
           "A",
           "C",
           "B",
           "A",
           "D",
           "A",
           "C",
           "B",
           "D",
           "C",
           "D",
           "A",
           "D",
           "B",
           "D",
           "B",
           "B",
           "C",
           "D",
           "A",
           "C",
           "C",
           "C",
           "D",
           "A",
           "A",
           "A",
           "C",
           "B",
           "C",
           "D",
           "A",
           "A",
           "D",
           "B",
           "D",
           "A",
           "B",
           "C",
           "B",
           "B",
           "B",
           "B",
           "B",
           "D",
           "A",
           "B",
           "C",
           "A",
           "C",
           "B",
           "D",
           "B",
           "D",
           "D",
           "D",
           "D",
           "D",
           "A",
           "C",
           "B",
           "A",
           "B",
           "C",
           "C",
           "D",
           "A",
           "D",
           "A",
           "A",
           "A",
           "A",
           "B",
           "B",
           "B",
           "D",
           "B",
           "B",
           "B",
           "A",
           "C",
           "D",
           "A",
           "B",
           "B",
           "D",
           "C",
           "C",
           "D",
           "C",
           "B",
           "C",
           "A",
           "A",
           "B",
           "C",
           "A",
           "B",
           "C",
           "B",
           "D",
           "B",
           "C",
           "A",
           "D",
           "D",
           "D",
           "A",
           "A",
           "C",
           "B",
           "A",
           "D",
           "B",
           "D",
           "C",
           "A",
           "C",
           "C",
           "B",
           "A",
           "A",
           "A",
           "B",
           "A",
           "D",
           "A",
           "C",
           "A",
           "D",
           "D",
           "B",
           "C",
           "A",
           "D",
           "B",
           "B",
           "B",
           "D",
           "C",
           "D",
           "D",
           "D",
           "B",
           "C",
           "B",
           "D",
           "B",
           "B",
           "C",
           "C",
           "C",
           "A",
           "C",
           "D",
           "B",
           "D",
           "D",
           "B",
           "A",
           "C",
           "A",
           "C",
           "D",
           "A",
           "B",
           "C",
           "D",
           "C",
           "D",
           "A",
           "B",
           "C",
           "B",
           "A",
           "C",
           "D",
           "B",
           "D",
           "A",
           "C",
           "D",
           "B",
           "A",
           "C",
           "B",
           "D",
           "D",
           "C",
           "B",
           "A",
           "C",
           "D",
           "C",
           "B",
           "D",
           "A",
           "D",
           "A",
           "B",
           "D",
           "B"]

questions = [
    ("Information technology can be used to support ___.",
        ["A. product development teams",
         "B. customer support processes",
         "C. any other business activity",
         "D. All the choices are correct."]
    ),
    ("In its simplest form, a system consists of all the following except:",
     ["A. A group of cooperative users",
      "B. A set of interrelated components",
      "C. A clearly defined boundary",
      "D. A common set of objectives"]
     ),
    ("According to the Real World case, eCourier embraced technology by:",
     ["A. Doing the same things that all their competitors were doing successfully.",
      "B. Installing a new computerized bar-scanning system for packages.",
      "C. Enabling a new telephone system for customers.",
      "D. Giving all their couriers handheld GPS units for tracking and communication."]
     ),
    ("According to the Real World case, eCourier uses SeeWhy software to:",
     ["A. Track packages that have not been delivered.",
      "B. Provide business intelligence in terms of customer satisfaction.",
      "C. Interface with their accounting software.",
      "D. All of the above."]
     ),
    ("According to the Real World Case, the goal of Bryan Cave is:",
     ["A. To have the best value for their customers.",
      "B. To create increased profit per customer.",
      "C. To build the best long-term relationships in the world.",
      "D. All the above."]
     ),
    (
        "According to the Real World Case, the Bryan Cave law firm had difficulty billing its real estate customers because:",
        ["A. The developers could not afford their rates.",
         "B. Developers think in terms of square feet, not hours worked.",
         "C. Their lawyers did not understand the real estate profession.",
         "D. None of the above."]
    ),
    ("According to the Real World Case, the big problem facing the Bryan Cave law firm in 2002 was:",
     ["A. Communications between all their lawyers and offices.",
      "B. Dealing with the differences in laws around the world.",
      "C. Billing their clients correctly.",
      "D. Making the highest profits from their resources while delivering the highest customer value."]
     ),
    ("All the following are examples of an information system, except:",
     ["A. A day planner",
      "B. A cash register",
      "C. A group of marbles in a box",
      "D. A paper-based accounting ledger"]
     ),
    (
        "According to the text, most retail stores today use computer-based information systems to support business processes and operations. This support falls broadly into the categories of:",
        ["A. Business decisions and strategies for competitive advantage.",
         "B. Operations and support strategies.",
         "C. Business decisions and operations.",
         "D. Strategic business decisions and tactical business decisions."]
    ),
    ("How do information systems aid in decision making?",
     ["A. Information systems help companies determine investments.",
      "B. Information systems help companies determine which products to sell or discontinue.",
      "C. Information systems can be used to gain competitive advantage.",
      "D. All of the choices are correct."]
     ),
    (
        "All of the following are fundamental reasons for business applications of information technology except:",
        ["A. Support of strategies for competitive advantage",
         "B. Support of business processes and operations",
         "C. Compliance with environmental regulations",
         "D. Decision making support"]
    ),
    ("According to the textbook case, Welch's uses BI software from Oco to:",
     ["A. manage their gasoline usage.",
      "B. decide which products should be produced.",
      "C. ensure that its carriers are shipping full truckloads to customers.",
      "D. follow new competitive trends from its competitors."]
     ),
    ("According to the textbook case, the Oco BI software used by Welch's:",
     ["A. increases the number of deliveries made on Fridays.",
      "B. assures that most deliveries are not made on Fridays.",
      "C. assures that most deliveries are made on Fridays.",
      "D. helps them even out the number of delivery trucks used each day of the week."]
     ),
    (
        "The expanding role of information systems from the 1950s to the present, in sequential order, are:",
        [
            "A. Management reporting, decision support, electronic business and commerce, data processing, strategic and end user support",
            "B. Data processing, management reporting, strategic and end user support, electronic business and commerce, decision support",
            "C. Data processing, management reporting, decision support, strategic and end user support, electronic business and commerce",
            "D. Electronic business and commerce, management reporting, data processing, strategic and end user support, decision support"]
    ),
    (
        "The rapid development of microcomputer processing power, application software packages, and telecommunications networks gave birth to the phenomenon of ___.",
        ["A. manufacturer-to-public direct sales",
         "B. MIS departments",
         "C. end user computing",
         "D. electronic monitoring"]
    ),
    ("Which of the following is a false statement?",
     ["A. Today's information systems are doing the same basic things that they did over 40 years ago.",
      "B. Today there is a much higher level of integration of system functions.",
      "C. Today there is greater connectivity across dissimilar system components.",
      "D. None of the statements is false."]
     ),
    ("Companies generally rely on e-business applications to do all of the following except:",
     ["A. Re-engineer internal business processes",
      "B. Implement electronic commerce systems",
      "C. Monitor employee productivity",
      "D. Promote enterprise collaboration among business teams and workgroups"]
     ),
    ("In an e-business enterprise, an intranet refers to:",
     ["A. An Internet-like network inside the enterprise",
      "B. A network between an enterprise and its trading partners",
      "C. A network between the members of a single workgroup",
      "D. All the choices are correct."]
     ),
    ("E-business uses Internet technologies to work and empower ___.",
     ["A. business processes",
      "B. electronic commerce",
      "C. collaboration among business teams",
      "D. All of the choices are correct."]
     ),
    ("E-commerce ___.",
     [
         "A. involves buying, selling, marketing, and servicing of products, services, and information over a variety of computer networks",
         "B. uses the Internet, intranets, and extranets to support every step of the commercial process, such as multimedia advertising, product information, and customer support",
         "C. involves Internet security and payment mechanisms that ensure completion of delivery and payment processes",
         "D. All of the choices are correct."]
     ),
    (
        "The text classifies information systems as either operations or management support information systems. Which one of the following would not be classified as an operations support system?",
        ["A. Transaction processing systems",
         "B. Process control systems",
         "C. Enterprise collaboration systems",
         "D. Decision support systems"]
    ),
    ("Electronic commerce systems generally include all of the following except:",
     ["A. Internet websites for online sales",
      "B. Direct links to credit reporting services",
      "C. Extranet access of inventory databases",
      "D. Intranets that allow sales reps to access customer records"]
     ),
    ("Process control systems monitor and control ___ processes.",
     ["A. physical",
      "B. transactional",
      "C. inter-departmental",
      "D. mechanical"]
     ),
    (
        "A nuclear power plant uses electronic sensors linked to computers to continually monitor processes and make instant (real-time) adjustments that control the power generation process. This is an example of a(n) ___.",
        ["A. transaction processing system",
         "B. decision support system",
         "C. enterprise collaboration system",
         "D. process control system"]
    ),
    (
        "When employees in a project team use email to send and receive messages and use video conferences to hold electronic meetings and coordinate their activities, they are using ___.",
        ["A. transaction processing systems",
         "B. process control systems",
         "C. enterprise collaboration systems",
         "D. decision support systems"]
    ),
    (
        "A database of customer purchases that provides end-user managers with interactive and ad hoc decision-making support is referred to as ___.",
        ["A. a transaction processing system",
         "B. a decision support system",
         "C. an information reporting system",
         "D. an executive information system"]
    ),
    (
        "A production manager needs a system to help determine how much product to manufacture based on the expected sales associated with a future promotion, plus the location and availability of the raw materials necessary to manufacture the product. What type of system would meet this manager's needs?",
        ["A. Transaction processing system",
         "B. Process control system",
         "C. Enterprise collaboration system",
         "D. Decision support system"]
    ),
    (
        "When information system applications focus on providing information and support for effective decision making by managers, they are called ___ support systems.",
        ["A. decision",
         "B. management",
         "C. collaboration",
         "D. process"]
    ),
    (
        "An information system that supports the business functions of accounting, finance, human resource management, marketing, or operations would be classified as a(n) ___ system.",
        ["A. functional business",
         "B. executive information",
         "C. management information",
         "D. decision support"]
    ),
    (
        "Information systems that focus on operational and managerial applications in support of basic business functions, such as accounting or marketing, are known as ___.",
        ["A. functional business systems",
         "B. strategic information systems",
         "C. executive information systems",
         "D. knowledge management systems"]
    ),
    ("Most information systems are designed to ___.",
     ["A. produce information and support decision making",
      "B. handle record-keeping",
      "C. handle transaction processing chores",
      "D. All the choices are correct."]
     ),
    (
        "Executive information systems (EIS) are tailored to meet the strategic information needs of which of the following management levels?",
        ["A. Top management (strategic)",
         "B. Middle management (tactical)",
         "C. Lower management (operational)",
         "D. All of the choices are correct."]
    ),
    (
        "Business applications of information systems are typically combinations of several types of information systems. This integration is referred to as ___ systems.",
        ["A. information reporting",
         "B. decision support",
         "C. cross-functional informational",
         "D. end user computing"]
    ),
    (
        "Success in today's dynamic business environment depends heavily on maximizing the use of Internet-based technologies and Web-enabled information systems to meet the competitive requirements of ___.",
        ["A. customers",
         "B. suppliers",
         "C. business partners",
         "D. All of the choices are correct."]
    ),
    ("A functional business system supports all of the following types of applications except:",
     ["A. Accounting",
      "B. Customer problem resolution",
      "C. Marketing",
      "D. Human resource management"]
     ),
    ("Which of the following systems acts as a consultant to users?",
     ["A. Knowledge",
      "B. Integrated information",
      "C. Executive information",
      "D. Expert"]
     ),
    (
        "According to the textbook case on responsibility and accountability, even if a project is not an IT project, who is held responsible for optimizing returns on IT-related investments?",
        ["A. CEO",
         "B. CFO",
         "C. COO",
         "D. CIO"]
    ),
    ("According to the textbook case on responsibility and accountability:",
     ["A. IT is always 100% responsible for any large project involving information technology.",
      "B. IT is never 100% responsible for any large project involving information technology.",
      "C. IT is sometimes 100% responsible for any large project involving information technology.",
      "D. None of the above is correct."]
     ),
    ("Developing an information system solution involves all of the following steps except:",
     ["A. Investigation",
      "B. Implementation",
      "C. Redesign",
      "D. Maintenance"]
     ),
    (
        "Computer-based information systems are usually conceived, designed, and implemented using some form of systematic development process. The investigation stage includes ___.",
        ["A. determining the economic or technical feasibility of a proposed application",
         "B. acquiring and learning how to use the necessary software",
         "C. improving the system",
         "D. All of the choices are correct."]
    ),
    (
        "Developing information system solutions to business problems in an organization is the responsibility of ___.",
        ["A. information system specialists",
         "B. computer programmers",
         "C. systems analysts",
         "D. all information system users within the organization"]
    ),
    (
        "When applying a systematic development process for computer-based information systems, ___ would be part of the analysis phase.",
        ["A. determining the business requirements of the system",
         "B. acquiring and learning how to use the necessary software",
         "C. implementing a trial system",
         "D. obtaining feedback from end users of the system"]
    ),
    (
        "According to the text, the steps of developing an information system, in their proper order, are:",
        ["A. Investigate, analyze, implement, design, maintain",
         "B. Investigate, design, analyze, implement, maintain",
         "C. Maintain, implement, design, analyze, investigate",
         "D. Investigate, analyze, design, implement, maintain"]
    ),
    (
        "In the lawsuit filed against Hannaford Brothers, which of the following was not alleged as a reason for filing the suit?",
        ["A. Hannaford has installed inadequate security measures.",
         "B. Hannaford did not disclose the security breach to the public quickly enough.",
         "C. Hannaford sold the data to spammers.",
         "D. All the choices are correct."]
    ),
    (
        "The information systems function is equally as important to business success as the function of ___.",
        ["A. accounting",
         "B. operations management",
         "C. human resources management",
         "D. All the choices are correct."]
    ),
    ("In the information systems concept, the processing function involves:",
     ["A. Capturing and assembling elements that enter the system to be processed",
      "B. Transformation processes that convert input into output",
      "C. Transferring elements that have been produced by a transformation process to their ultimate destination",
      "D. Monitoring and evaluating feedback to determine whether a system is moving toward the achievement of its goal"]
     ),
    (
        "According to the Real World case about the New York Times, the newspaper industry is in very deep trouble. What has become most important to them?",
        ["A. Business model innovation",
         "B. Internet connectivity",
         "C. Technological innovation",
         "D. Communication initiatives"]
    ),
    ("If a system is one of the components of a larger system, it is considered a(n) ___.",
     ["A. environment",
      "B. feedback loop",
      "C. subsystem",
      "D. interface"]
     ),
    ("A system that can change itself or its environment in order to survive is ___ system.",
     ["A. a control",
      "B. a self-monitoring",
      "C. an environmental",
      "D. an adaptive"]
     ),
    (
        "Organizations are examples of ___ systems because they interface and interact with other systems in their environment.",
        ["A. linked",
         "B. open",
         "C. dependent",
         "D. parallel"]
    ),
    ("The majority of organizations today would be classified as ___ systems.",
     ["A. open",
      "B. closed",
      "C. open adaptive",
      "D. closed adaptive"]
     ),
    ("An information system depends on all of the following resources except:",
     ["A. Hardware",
      "B. Software",
      "C. People",
      "D. Time"]
     ),
    ("All of the following would be considered a hardware resource except:",
     ["A. A microcomputer",
      "B. A keyboard",
      "C. Magnetic and optical disks",
      "D. Programs and procedures"]
     ),
    ("All of the following would be considered a software resource in an information system except:",
     ["A. A computer operating system",
      "B. A word processing software package",
      "C. A telecommunication network",
      "D. All of the choices are software resources."]
     ),
    (
        "In an information system context, which one of the following would be the most applicable description of application software?",
        ["A. It controls and supports the operations of a computer",
         "B. It consists of programs that direct particular processing activities",
         "C. It consists of operating instructions for people who will use an information system",
         "D. None of the choices are correct."]
    ),
    ("In an information system, alphanumeric data normally takes the form of ___.",
     ["A. numbers and alphabetical characters",
      "B. sentences and paragraphs",
      "C. graphic shapes and figures",
      "D. All of the choices are correct."]
     ),
    ("In an information system, image data normally takes the form of ___.",
     ["A. numbers and alphabetical characters",
      "B. sentences and paragraphs",
      "C. graphic shapes and figures",
      "D. voice and other sounds"]
     ),
    ("All of the following are good examples of information except:",
     ["A. The social security number of the company's forklift operator",
      "B. The retail price of blue widgets",
      "C. How much the company owes to vender number 17",
      "D. The numbers 1236789, 349875, and 340977"]
     ),
    ("Telecommunications networks consist of ___.",
     ["A. computers, the Internet, intranets, and extranets",
      "B. communications processors",
      "C. devices interconnected by communication media and controlled by communications software",
      "D. All of the choices are correct."]
     ),
    ("All of the following normally happens to data during a value-added process except:",
     ["A. Their useful life is determined",
      "B. Their form is aggregated, manipulated, and organized",
      "C. Their content is analyzed and evaluated",
      "D. They are placed in a proper context for a human user"]
     ),
    ("All of the following are considered computer hardware technology except:",
     ["A. Operating system software",
      "B. Microcomputers",
      "C. Keyboards",
      "D. Printers"]
     ),
    ("Which of the following is an example of control of an information system's performance?",
     ["A. A system malfunction wiped out two weeks of student registration records",
      "B. Programmers created a user friendly input screen for a new system",
      "C. Subtotals do not add up to total sales; IT staff investigates whether data entry or processing is the problem",
      "D. An extra $20 was added to every water bill by mistake"]
     ),
    ("The original, formal record of a transaction is called the:",
     ["A. Updated form",
      "B. Paper form",
      "C. Transaction document",
      "D. Source document"]
     ),
    ("The source document is:",
     ["A. The form of a document after its final update",
      "B. A transaction document that refers to the source of the product",
      "C. The original, formal record of a transaction",
      "D. The first update to any transaction"]
     ),
    (
        "A strategic information system can be any kind of information system that uses information technology to help an organization ___.",
        ["A. gain a competitive advantage",
         "B. reduce a competitive disadvantage",
         "C. meet strategic enterprise objectives",
         "D. all of the choices are correct."]
    ),
    (
        "A firm can survive and succeed in the long run if it successfully develops strategies to confront the ___ that shape the structure of competition in its industry.",
        ["A. technological innovations",
         "B. competitive business processes",
         "C. competitive forces",
         "D. competitive strategies"]
    ),
    (
        "A(n) ___ strategy is a competitive strategy by which a firm seeks to become a low-cost producer of products and services in the industry.",
        ["A. cost leadership",
         "B. differentiation",
         "C. innovation",
         "D. alliance"]
    ),
    (
        "A(n) ___ strategy is a competitive strategy by which a firm develops ways to differentiate its products and services from those of its competitors.",
        ["A. low cost leadership",
         "B. innovation",
         "C. differentiation",
         "D. growth"]
    ),
    (
        "A(n) ___ strategy is a competitive strategy by which a firm develops unique products or services from those of its competitors, or makes radical business changes that may alter the fundamental nature of the industry.",
        ["A. alliance",
         "B. growth",
         "C. differentiation",
         "D. innovation"]
    ),
    (
        "A(n) ___ strategy is a competitive strategy by which a firm significantly expands its capacity to produce goods and services, expanding and diversifying in the market.",
        ["A. alliance",
         "B. growth",
         "C. differentiation",
         "D. innovation"]
    ),
    (
        "A(n) ___ strategy is a competitive strategy by which a firm establishes new business linkages with customers, suppliers, competitors, and other companies.",
        ["A. growth",
         "B. low cost leadership",
         "C. differentiation",
         "D. alliance"]
    ),
    ("According to the text, competition is a ___ characteristic in business that ___.",
     ["A. positive, is natural and healthy",
      "B. negative, can consume significant resources",
      "C. neutral, can help a firm meet strategic enterprise objectives",
      "D. none of the choices are correct."]
     ),
    ("According to the text, in the world of the Internet, a firm's biggest competitor:",
     ["A. Usually exists and is close in the physical world",
      "B. Usually does not exist but will emerge close in the physical world",
      "C. May not yet exist but could emerge almost overnight",
      "D. Probably exists in an overseas location"]
     ),
    ("According to the text, the Internet:",
     ["A. Has limited competition world-wide",
      "B. Has created many ways to enter the market quickly, with relatively low cost",
      "C. Has created new entry barriers to competition",
      "D. Has decreased prices world-wide"]
     ),
    ("Which of the following is a competitive strategy?",
     ["A. New entries into the market",
      "B. Innovation",
      "C. Bargaining power",
      "D. Substitutes"]
     ),
    ("All the following are competitive strategies except:",
     ["A. New entries into the market",
      "B. Innovation",
      "C. Cost leadership",
      "D. Alliances"]
     ),
    ("All of the following can be used to counter competitive forces in the marketplace except:",
     ["A. Alliances",
      "B. Growth",
      "C. Innovation",
      "D. Bargaining"]
     ),
    ("All of the following are competitive forces in the marketplace except:",
     ["A. Alliances",
      "B. Competition",
      "C. Substitutes",
      "D. Bargaining"]
     ),
    ("Which of the following is a competitive force in the marketplace?",
     ["A. Cost leadership",
      "B. Competition",
      "C. Differentiation",
      "D. Alliances"]
     ),
    (
        "Developing a relationship with a customer such that the customer cannot afford to switch suppliers is an example of:",
        ["A. Monopolistic enterprise",
         "B. Locking in the customer",
         "C. Growth strategies",
         "D. None of the above is correct"]
    ),
    (
        "The practice of becoming the largest purchaser of products from a given supplier is an example of:",
        ["A. Cost leadership",
         "B. Growth strategies",
         "C. Differentiation",
         "D. Locking in the supplier"]
    ),
    ("Becoming a low-cost producer of products and services in an industry is an example of a(n):",
     ["A. Cost leadership strategy",
      "B. Differentiation strategy",
      "C. Innovation strategy",
      "D. Growth strategy"]
     ),
    ("All of the following are basic competitive forces discussed in the text except:",
     ["A. Rivalry of competitors",
      "B. Threat of substitutes",
      "C. Bargaining power of suppliers",
      "D. Bargaining power of competitors"]
     ),
    ("All of the following are basic competitive strategies discussed in the text except:",
     ["A. Cost leadership",
      "B. Innovation",
      "C. Product differentiation",
      "D. Strategic dominance"]
     ),
    ("Expanding a company's product offering into global markets is an example of a(n) ___ strategy.",
     ["A. cost leadership",
      "B. differentiation",
      "C. growth",
      "D. alliance"]
     ),
    ("Investments in information technology that build valuable new relationships allow a firm to:",
     ["A. Lock in the supplier",
      "B. Lock in the customer",
      "C. Lock out competition",
      "D. All the above"]
     ),
    (
        "In addition to the five basic competitive strategies, the text describes several key strategies implemented with information technology. Which of the following is not one of those strategies?",
        ["A. Locking in customers",
         "B. Building switching costs",
         "C. Creating alliances",
         "D. Raising barriers to entry"]
    ),
    (
        "Using an information system to make customers and/or suppliers reluctant to change to another competitor is called:",
        ["A. Growth strategy",
         "B. Building switching costs",
         "C. Creating alliances",
         "D. Raising barriers to entry"]
    ),
    (
        "When a firm develops ways to differentiate their products and services from their competitors', it is pursuing a ___ strategy.",
        ["A. differentiation",
         "B. alliance",
         "C. innovation",
         "D. marketing"]
    ),
    ("A sales company such as eBay would be most likely to use information technology to promote ___.",
     ["A. online stock trading",
      "B. point-of-sale inventory tracking",
      "C. online auctions",
      "D. virtual manufacturing alliances"]
     ),
    (
        "When a firm strives to find ways to help its suppliers and customers reduce their costs or to increase the costs of their competitors, it is pursuing a strategy of ___.",
        ["A. innovation",
         "B. alliance",
         "C. cost leadership",
         "D. growth"]
    ),
    (
        "When customers become dependent on mutually beneficial inter-enterprise information systems, they become reluctant to switch to a company's competitors because they would incur all following costs except:",
        ["A. Time",
         "B. Money",
         "C. Innovation",
         "D. Effort"]
    ),
    (
        "Companies like Wal-Mart extend their networks to their customers and suppliers in order to build innovative continuous inventory replenishment systems that would lock in their business. This creates a(n) ___ information system.",
        ["A. leveraged",
         "B. inter-enterprise",
         "C. intra-enterprise",
         "D. locked-in"]
    ),
    ("A serious problem of competitive advantage is that:",
     ["A. It normally doesn't last very long and it isn't sustainable over the long term",
      "B. Competitors figure out how it was done and do the same thing",
      "C. A competitive advantage can become a competitive necessity",
      "D. All of the choices are correct."]
     ),
    (
        "A company that places a strategic focus on customer value recognizes that ___, rather than ___, has become a primary determinant in a customer's perception of value.",
        ["A. service, price",
         "B. price, quality",
         "C. quality, service",
         "D. quality, price."]
    ),
    (
        "Companies that consistently offer the best value from the customer's perspective do all the following, except:",
        ["A. Keep track of their customers' individual preferences",
         "B. Keep up with market trends",
         "C. Supply products, services, and information anytime, anywhere",
         "D. Offer lowest prices and fastest delivery"]
    ),
    ("A customer-focused business can build customer value and loyalty by:",
     ["A. Making a loyal customer feel special with website personalization",
      "B. Letting customers place orders directly, or through distribution partners",
      "C. Letting customers check order history and delivery status",
      "D. All of the choices are correct."]
     ),
    ("A transaction database allows all of the following activities except:",
     ["A. Linking employees and distribution partners to customers",
      "B. Letting customers check order history",
      "C. Giving employees a complete view of each customer",
      "D. None of these activities are supported by a transaction database."]
     ),
    (
        "According to the textbook case, innovation in information systems at Universal Orlando comes from thinking like a:",
        ["A. Customer",
         "B. Competitor",
         "C. Employee",
         "D. IT specialist"]
    ),
    (
        "The value chain framework can be used to view a firm as a series, a chain, or a network of basic activities that:",
        ["A. Add value to its products and services, and thus add a margin of value to the firm.",
         "B. Lower costs along the product development chain.",
         "C. Create the perception of value and goodwill to employees.",
         "D. Create a smooth-flowing chain of events between the supplier and the customer."]
    ),
    ("Which of the following is a primary business process?",
     ["A. Collaborative workflow intranet",
      "B. Targeted marketing",
      "C. Technology development",
      "D. Procurement of resources"]
     ),
    ("All of the following are primary business processes, except:",
     ["A. Customer relationship management",
      "B. Targeted marketing",
      "C. Technology development",
      "D. Just-in-time warehousing"]
     ),
    ("Which of the following is a support process?",
     ["A. Collaborative workflow intranet",
      "B. Targeted marketing",
      "C. Customer relationship management",
      "D. Just-in-time warehousing"]
     ),
    ("All of the following are support processes, except:",
     ["A. Customer relationship management",
      "B. Procurement of resources",
      "C. Technology development",
      "D. Employee benefits intranet"]
     ),
    ("Business process reengineering is best defined as:",
     ["A. A key technology to reduce customer late payments",
      "B. A radical redesign of business processes to achieve improvements in cost, quality, speed, or service",
      "C. A key way to ensure successful improvement in processing",
      "D. All of the choices are correct."]
     ),
    ("Business process reengineering (BPR) is often referred to as:",
     ["A. Streamlining",
      "B. Reengineering",
      "C. Quickening",
      "D. None of the choices are correct."]
     ),
    ("Business process reengineering (BPR) incorporates all the following strategies, except:",
     ["A. Lowering prices as a competitive strategy",
      "B. Promoting business innovation",
      "C. Making major improvements to business operations",
      "D. None of the choices are correct."]
     ),
    ("Traditional business improvement includes:",
     ["A. Top-down participation",
      "B. Long time requirements",
      "C. Brand new business processes",
      "D. Incremental levels of change"]
     ),
    ("Business process engineering includes:",
     ["A. Bottom-up participation",
      "B. Short time requirements",
      "C. Improved new versions of current processes",
      "D. Radical levels of change"]
     ),
    ("Traditional business improvement includes all the following, except:",
     ["A. Bottom-up participation",
      "B. Short time requirements",
      "C. Improved new versions of current processes",
      "D. Radical levels of change"]
     ),
    ("Business process redesign includes all the following, except:",
     ["A. Top-down participation",
      "B. Long time requirements",
      "C. Brand new business processes",
      "D. Incremental levels of change"]
     ),
    (
        "Organizations are changing from a competitive environment in which mass-market products and services were standardized, long-lived, information-poor, and exchanged in one-time transactions to an environment in which companies compete globally with niche-market products and services that are ___.",
        ["A. individualized",
         "B. short-lived",
         "C. exchanged on an ongoing basis with customers",
         "D. All the choices are correct."]
    ),
    ("An agile company supports all the following except:",
     ["A. Short-lived products and services",
      "B. Standardized products and services",
      "C. Information-rich products and services",
      "D. Niche market products and services"]
     ),
    ("___ agility is the ability to co-opt customers in the exploitation of innovation opportunities.",
     ["A. Customer",
      "B. Partnering",
      "C. Operational",
      "D. Technological"]
     ),
    (
        "___ agility is the ability to leverage assets, knowledge, and competencies in the exploration and exploitation of innovation opportunities.",
        ["A. Customer",
         "B. Partnering",
         "C. Operational",
         "D. Technological"]
    ),
    (
        "___ agility is the ability to accomplish speed, accuracy, and cost economy in the exploitation of innovation opportunities.",
        ["A. Customer",
         "B. Partnering",
         "C. Operational",
         "D. Technological"]
    ),
    ("Which of the following is not a strategy of a virtual company?",
     ["A. Share infrastructure and risk with alliance partners",
      "B. Link complementary core competencies",
      "C. Migrate from selling products to selling solutions",
      "D. Increase concept-to-case time"]
     ),
    ("Explicit knowledge deals with:",
     ["A. Data, documents, and things written down or stored on computers.",
      "B. How - to knowledge, which resides in workers.",
      "C. Using data mining techniques to capture external information.",
      "D. All of the choices are correct."]
     ),
    ("Tacit knowledge deals with:",
     ["A. Data, documents, and things written down or stored on computers.",
      "B. How - to knowledge, which resides in workers.",
      "C. Using data mining techniques to capture external information.",
      "D. None of the choices are correct."]
     ),
    ("Accessing and retrieving documents that have been stored online is a function of ___.",
     ["A. document management",
      "B. enterprise intelligence",
      "C. information creation, sharing, and management",
      "D. All of the choices are correct."]
     ),
    ("Real-time information management, communication, and collaboration are a function of ___.",
     ["A. document management",
      "B. enterprise intelligence",
      "C. information creation, sharing, and management",
      "D. All of the choices are correct."]
     ),
    (
        "Performance support, building expert networks, and leveraging organizational know-how are a function of ___.",
        ["A. document management",
         "B. enterprise intelligence",
         "C. information creation, sharing, and management",
         "D. All of the choices are correct."]
    ),
    (
        "The goal of knowledge management systems (KMS) is to help knowledge workers ___ important business knowledge.",
        ["A. create",
         "B. organize",
         "C. distribute",
         "D. All of the choices are correct."]
    ),
    (
        "According to the textbook case, the Matter Page System at Goodwin Proctor increases efficiency of their attorneys by.",
        ["A. Separating the client billing, documents, and contact data",
         "B. Enabling the attorneys to launch more than one application at a time to find information",
         "C. Requiring the attorneys to spend more time researching their cases",
         "D. Pulling all the client billing, documents and contact data into a single one - stop - shop for users"]
    ),
    ("Computer systems rely on all the following components except ___.",
     ["A. input",
      "B. internet",
      "C. processing",
      "D. storage"]
     ),
    ("Computer systems rely on which of the following components?",
     ["A. Input, processing, output, storage, and control",
      "B. Input, processing, output, storage, and the Internet",
      "C. The Internet, processing, output, storage, and control",
      "D. Input, processing, output, the Internet, and control"]
     ),
    ("The mechanical loom was invented by ___.",
     ["A. Blaise Pascal",
      "B. Joseph Jacquard",
      "C. Herman Hollerith",
      "D. Keith Glennan"]
     ),
    ("The first generation of computers relied on ___.",
     ["A. miniaturized circuits",
      "B. transistors",
      "C. vacuum tubes",
      "D. punch cards"]
     ),
    ("The second generation of computers relied on ___.",
     ["A. miniaturized circuits",
      "B. transistors",
      "C. vacuum tubes",
      "D. punch cards"]
     ),
    (
        "In the 1950s, ___ were invented and quickly replaced the thousands of vacuum tubes used in electronic computers.",
        ["A. microchips",
         "B. resistors",
         "C. transistors",
         "D. miniaturized circuits"]
    ),
    ("The third generation of computers relied on ___.",
     ["A. solid state technology and integrated circuits",
      "B. transistors",
      "C. vacuum tubes",
      "D. punch cards"]
     ),
    ("The first electronic digital computer was completed in the ___.",
     ["A. 1870s",
      "B. 1940s",
      "C. 1950s",
      "D. 1960s"]
     ),
    (
        "The ___ generation of computers was characterized by further miniaturization of circuits, increased multiprogramming, and virtual storage memory.",
        ["A. second",
         "B. third",
         "C. fourth",
         "D. fifth"]
    ),
    (
        "___ are the most important category of computer systems for both businesspeople and individual consumers.",
        ["A. Microcomputers",
         "B. Supercomputers",
         "C. Network Servers",
         "D. Mainframes"]
    ),
    (
        "According to the text, which of the following is considered by millions of computer users to be the primary function of the desktop PC?",
        ["A. Allows access to the Internet",
         "B. Increases productivity through the use of software applications",
         "C. Facilitates creation of local area networks",
         "D. All of the choices are correct"]
    ),
    ("Which of the following statements best describes a workstation computer?",
     [
         "A. Supports applications with heavy mathematical computing and graphics display demands, such as computer-aided design (CAD)",
         "B. Coordinates telecommunications and resource sharing in small, local area networks (LANS)",
         "C. Allows convenient mobile communications and touch-screen computing",
         "D. All of the choices are correct."]
     ),
    (
        "___ are some of the more powerful microcomputers; they are used to coordinate telecommunications and resource sharing in small LANs and in Internet and intranet websites.",
        ["A. Mainframes",
         "B. Supercomputers",
         "C. Network Servers",
         "D. None of the choices are correct."]
    ),
    (
        "According to the text, using web-enabled PDAs allows workers to realize all the following benefits except:",
        ["A. Send and receive email",
         "B. Access the Web",
         "C. Exchange information with desktop PCs or Web servers",
         "D. Helps retain younger and more technologically savvy employees"]
    ),
    (
        "An intelligent terminal that can perform data entry and some information processing tasks independently is called a ___ terminal.",
        ["A. transaction",
         "B. dumb",
         "C. Windows",
         "D. remote"]
    ),
    ("Which of the following does not apply to a personal digital assistant (PDA)?",
     ["A. Supports applications with heavy mathematical computing",
      "B. Touchscreens",
      "C. Pen-based handwriting recognition",
      "D. Web access"]
     ),
    ("Personal digital assistants most commonly use which of these technologies?",
     ["A. Pen-based computing",
      "B. Optical scanning",
      "C. Jump drives",
      "D. Back-lit keyboards"]
     ),
    ("What sets the RIM BlackBerry apart from other wireless PDA solutions?",
     ["A. Lower price",
      "B. It is always on and connected",
      "C. Smaller size and weight",
      "D. Longer battery life"]
     ),
    ("A BlackBerry ___.",
     ["A. performs common PDA functions",
      "B. doesn't have a visible antenna",
      "C. uses the same network as most mobile phones",
      "D. All of the choices are correct."]
     ),
    ("___ are high-end network servers that handle large-scale processing of business applications.",
     ["A. Midrange computers",
      "B. Mainframes",
      "C. Supercomputers",
      "D. All of the choices are correct."]
     ),
    (
        "___ are popular as powerful network servers to help manage large Internet Websites, intranets, and extranets.",
        ["A. Workstations",
         "B. Minicomputers",
         "C. Supercomputers",
         "D. Mainframes"]
    ),
    ("Which of the following is a common application for a midrange computer?",
     ["A. Internet functions.",
      "B. Integrated enterprise-wide manufacturing and distribution.",
      "C. Financial applications.",
      "D. All of the choices are correct."]
     ),
    ("According to the text, which of the following is not true of Mainframes?",
     ["A. Mainframes can process thousands of million instructions per second (MIPS).",
      "B. Mainframes are large, fast, and powerful.",
      "C. Mainframes have large storage capacities.",
      "D. All of the choices are correct."]
     ),
    ("Which of the following would not be considered a characteristic of supercomputer systems?",
     ["A. Costs between $5 million and $50 million.",
      "B. Used for global weather reports and military defense.",
      "C. Runs the same software found on most home computers, but at faster speeds",
      "D. Designed specifically for high-speed numeric computation"]
     ),
    ("The function of an input device is:",
     ["A. to interpret computer program instructions",
      "B. to transmit directions to other components of the computer system",
      "C. to convert data into electronic form for entry into a computer system",
      "D. none of the above"]
     ),
    ("The central processing unit (CPU):",
     ["A. is the main processing component of a computer system",
      "B. controls all the peripheral devices of a computer system",
      "C. is controlled by the RAID unit",
      "D. is also called a Fuzzy Logic unit"]
     ),
    ("The output devices of a computer system include:",
     ["A. printers and video displays",
      "B. the Arithmetic-logic unit",
      "C. scanners and RAID units",
      "D. the Fuzzy Logic unit"]
     ),
    ("The central processing unit (CPU) consists of:",
     ["A. the Control unit and the RAID unit",
      "B. Arithmetic-logic unit and the RAID unit",
      "C. the RAID unit and the Fuzzy Logic unit",
      "D. the Control unit and the Arithmetic-logic unit"]
     ),
    (
        "Which of the following would perform the required mathematical and logic operations of a central processing unit (CPU)?",
        ["A. Control unit",
         "B. Arithmetic-logic unit",
         "C. RAID unit",
         "D. Fuzzy logic unit"]
    ),
    ("The function of an output device is to:",
     [
         "A. Convert data into an electronic machine-readable form for direct entry into a computer system",
         "B. Perform the arithmetic and logic functions required in computer processing",
         "C. Convert electronic information produced by the computer system into human-intelligible form for presentation to end-users",
         "D. Store the data and program instructions needed for processing"]
     ),
    ("Which of the following is a secondary storage device?",
     ["A. Primary memory",
      "B. Random access memory",
      "C. Magnetic disk",
      "D. The CPU"]
     ),
    ("According to Moore's Law, ___ doubles every 18 to 24 months.",
     ["A. computing power",
      "B. computer prices",
      "C. computer storage capacity",
      "D. the number of functioning computers"]
     ),
    ("Which of the following would not fit the typical classification of a computer peripheral?",
     ["A. Monitors and printers",
      "B. Scanners and hard disk drives",
      "C. CD-ROM drives and backup systems",
      "D. Central processing unit"]
     ),
    ("Offline devices:",
     ["A. are directly attached to the CPU",
      "B. are not controlled by the CPU",
      "C. are controlled by the CPU",
      "D. can replace the CPU"]
     ),
    ("The most popular pointing device used today is the ___.",
     ["A. pointing stick",
      "B. light pen",
      "C. trackball",
      "D. electronic mouse"]
     ),
    ("All of the following relate to Peripherals except:",
     ["A. input devices",
      "B. output devices",
      "C. CPU devices",
      "D. secondary storage devices"]
     ),
    (
        "One device used as an input device in a computer system is a pointing stick, which is best described as:",
        ["A. A small gearshift lever set in a box",
         "B. A stationary device containing a roller ball whose top is exposed outside its case",
         "C. A pen-shaped device with a ballpoint at the end",
         "D. A small, button-like device, sometimes likened to the eraser head of a pencil"]
    ),
    ("A touchpad is best described as a:",
     ["A. Small, rectangular, touch-sensitive surface usually placed below the keyboard",
      "B. Stationary device containing a roller ball whose top is exposed outside its case",
      "C. Pen-shaped device with a ballpoint at the end",
      "D. Device rolled along the desktop in order to move the cursor on the screen"]
     ),
    ("Continuous speech recognition systems:",
     ["A. Compare speech patterns to a dictionary",
      "B. Allow a computer to understand a few words from a voice it has never heard before",
      "C. Require users to pause between each spoken word",
      "D. Recognize conversationally paced speech"]
     ),
    (
        "Speech recognition devices in work situations allow operators to perform all the following except:",
        ["A. Enter data without using their hands.",
         "B. Input data faster.",
         "C. input data more accurately.",
         "D. Input data without using a computer."]
    ),
    ("Speaker independent voice recognition systems:",
     ["A. Compare speech patterns to a dictionary",
      "B. Allow a computer to understand a few words from a voice it has never heard before",
      "C. Require users to pause between each spoken word",
      "D. All of the choices are correct."]
     ),
    ("Which of the following best describes optical scanning devices?",
     ["A. Hand-held wands used to read data on merchandise tags",
      "B. Photoelectric devices that scan data",
      "C. Converts reflected light patterns into electronic impulses, which are accepted as input into the computer system",
      "D. All of the choices are correct."]
     ),
    ("Which of the following best describes magnetic stripe technology?",
     ["A. A form of data entry that helps computers read credit cards",
      "B. A form of computing where debit and credit cards have an embedded microprocessor chip",
      "C. Technology that enables users to download full-motion video into a computer system",
      "D. Technology commonly used in banks in order to magnetically read checks and deposit slips"]
     ),
    ("The dark, magnetic stripe on the back of credit cards can hold about ___ of information.",
     ["A. 200 gigabytes",
      "B. 200 kilobytes",
      "C. 200 bytes",
      "D. Immaterial, as this technology is not yet available in the United States"]
     ),
    ("Smart card technology:",
     [
         "A. Allows debit cards to store a cash balance on a card and electronically transfer some of it to others to pay for items and services",
         "B. Is not yet available in the United States",
         "C. Is commonly used by banks to read and process checks",
         "D. All of the choices are correct."]
     ),
    ("Banks use ___ technologies for check processing.",
     ["A. voice response",
      "B. magnetic ink character recognition",
      "C. laser printer",
      "D. optical scanner"]
     ),
    ("The most common output trend is ___.",
     ["A. printed reports and documents",
      "B. audio responses",
      "C. voice responses",
      "D. video displays"]
     ),
    ("Which of the following is not a valid storage medium?",
     ["A. Paper documents",
      "B. Optical disks",
      "C. Magnetic tape",
      "D. All of the choices are valid storage media."]
     ),
    ("High speed storage media ___ than lower-speed storage media.",
     ["A. cost less per byte and provide higher capacities",
      "B. cost less per byte and provide lower capacities",
      "C. cost more per byte and provide higher capacities",
      "D. cost more per byte and provide lower capacities"]
     ),
    ("___ bytes of storage are needed to represent the name \"Sarah.\"",
     ["A. Two",
      "B. Three",
      "C. Five",
      "D. Ten"]
     ),
    (
        "Data are processed and stored in a computer system through the presence or absence of electronic or magnetic signals to the computer. This is called a ___ representation of data, because the computer and the media can exhibit only two states or conditions.",
        ["A. Ternary",
         "B. Trinary",
         "C. Binary",
         "D. Bipolar"]
    ),
    (
        "Data are processed and stored in a computer system through the presence or absence of electronic or magnetic signals to the computer. This is called a binary representation of data, because the computer and the media can exhibit only ___ states or conditions.",
        ["A. two",
         "B. three",
         "C. five",
         "D. ten"]
    ),
    ("A bit, the smallest element of data, can have values of:",
     ["A. 0 or 1",
      "B. 0, 1, or 8",
      "C. 0 through 7",
      "D. 0 through 8"]
     ),
    ("A gigabyte (GB) is used to express which of the following approximate measures?",
     ["A. 1,000 byes of storage",
      "B. 1,000,000 bytes of storage",
      "C. 1,000,000,000 bytes of storage",
      "D. 1,000,000,000,000 bytes of storage"]
     ),
    ("Which of the following is an advantage of RAID?",
     ["A. It provides virtually unlimited online storage",
      "B. It provides high access speeds",
      "C. It provides fault-tolerant storage capacity",
      "D. All of the choices are advantages."]
     ),
    ("The primary storage (main memory) of a computer is also called:",
     ["A. ROM",
      "B. RAID",
      "C. RAM",
      "D. None of the choices are correct."]
     ),
    ("Which of the following storage types is volatile?",
     ["A. RAM",
      "B. ROM",
      "C. PROM",
      "D. All the choices are volatile."]
     ),
    ("Which of the following applies best to CD-RW optical disk technology?",
     ["A. Users are unable to record their own data on the disks",
      "B. Users can record their own data, but only once",
      "C. Users are able to record and then erase the disks",
      "D. None of the choices are correct."]
     ),
    ("Which of the following statements about optical disks is true?",
     ["A. They can be read only, recordable, or rewritable",
      "B. They can hold approximately 50 megabytes on a single disk",
      "C. They have totally replaced 3.5 diskettes",
      "D. They have totally replaced magnetic tape as secondary storage"]
     ),
    ("According to the text, what are the current types of RFID chips?",
     ["A. Electrical and magnetic",
      "B. Positive and negative",
      "C. Active and passive",
      "D. Red and Green"]
     ),
    ("Which of the following is true of off-the-shelf software?",
     ["A. It is developed with the intent to sell multiple copies",
      "B. The company buying the software has no control over the specifications, schedule, or evolution of the software",
      "C. The company that develops the software is not the intended audience",
      "D. All of the choices are correct."]
     ),
    (
        "Software is considered the ___ part of the computer, whereas the hardware is considered the ___ part.",
        ["A. expensive, inexpensive",
         "B. inexpensive, expensive",
         "C. variable, invariable",
         "D. invariable, variable"]
    ),
    ("The two general classifications of software are:",
     ["A. Systems and application",
      "B. Programming and CASE",
      "C. Commercial and custom",
      "D. Programming languages and development tools"]
     ),
    ("___ application programs perform common information processing jobs for end users.",
     ["A. Systems",
      "B. CASE",
      "C. Commercial",
      "D. General purpose"]
     ),
    (
        "___ software are programs that manage and support the operation of computer systems and networks.",
        ["A. System",
         "B. CASE",
         "C. Commercial",
         "D. General purpose"]
    ),
    ("An accounting program is an example of ___ software.",
     ["A. System",
      "B. CASE",
      "C. Application-specific",
      "D. General purpose"]
     ),
    ("According to the text, operating systems are a type of ___ program.",
     ["A. CASE",
      "B. System management",
      "C. Application-specific",
      "D. General purpose"]
     ),
    ("Application software can be subdivided into two categories:",
     ["A. COTS and POTS",
      "B. First generation and second generation",
      "C. Custom and commercial",
      "D. General purpose and function specific"]
     ),
    ("COTS software stands for:",
     ["A. Custom off-the-shelf software",
      "B. Commercial off-the-shelf software",
      "C. Combined off-the-shelf software",
      "D. Contaminated on-the-surface software"]
     ),
    (
        "According to the Real World Case, GE spends $150 million each year to purchase all of its desktop and laptop computers from how many vendors?",
        ["A. Two",
         "B. One",
         "C. Ten",
         "D. Nobody is certain"]
    ),
    (
        "According to the Real World Case, GE spends $150 million each year to purchase all of its desktop and laptop computers from which vendor?",
        ["A. Dell",
         "B. Hewlett-Packard",
         "C. Gateway",
         "D. None of the above"]
    ),
    ("According to the Real World Case, GE's Global Supplier Library lacked which of the following?",
     ["A. A central repository",
      "B. Multi-language capabilities",
      "C. Self-management of data",
      "D. All the above"]
     ),
    ("According to the Real World Case, which of the following is a problem with SaaS?",
     ["A. SaaS is open-source software.",
      "B. GE owns the software and is responsible for making it work daily.",
      "C. GE does not own the software, it's on lease. If the vendor goes bankrupt, everything shuts down.",
      "D. SaaS refuses to license its software to GE."]
     ),
    ("Which of the following are considered application software packages?",
     ["A. Word processing programs",
      "B. Operating systems",
      "C. System utilities",
      "D. System development programs"]
     ),
    ("Which of the following are considered general purpose application software packages?",
     ["A. Education and entertainment",
      "B. Electronic mail",
      "C. System utilities",
      "D. Programming languages"]
     ),
    ("Which of the following are considered application specific software packages?",
     ["A. Education and entertainment",
      "B. Electronic mail",
      "C. System utilities",
      "D. Programming languages"]
     ),
    ("Which of the following is not considered a system management software packages?",
     ["A. Database management",
      "B. CASE tools",
      "C. System utilities",
      "D. Application servers"]
     ),
    ("According to the text, which of the following describes system software?",
     ["A. Used for developing new systems as required for business purposes",
      "B. Performs information processing tasks for end users",
      "C. Allows anyone to contribute to the development of a specific application",
      "D. Manages and supports operations of computer systems and networks"]
     ),
    ("According to the text, function-specific application software does which of the following?",
     ["A. It supports specific applications of end users in business and other fields",
      "B. Provides CASE tools for developing new applications",
      "C. Allows anyone to contribute to the development of a specific application",
      "D. Manages and supports operations of computer systems and networks"]
     ),
    ("One of the biggest advantages offered by software suites is that:",
     ["A. All the programs within the suite use a similar graphical user interface (GUI)",
      "B. The packages take up a lot of disk space",
      "C. There is a custom graphical user interface for each application in the suite",
      "D. They cost more than the total cost of buying the individual packages separately"]
     ),
    ("Which of the following statements is not a characteristic of software suites?",
     [
         "A. They contain software tools that can help increase productivity, collaborate with colleagues, and access intranets, extranets, and the Internet",
         "B. All components of the software use a similar graphical user interface",
         "C. There is a custom graphical user interface for each application in the suite",
         "D. They cost less than the total cost of buying the individual packages separately"]
     ),
    ("Which of the following software suites is an open-source product?",
     ["A. Microsoft Office",
      "B. Lotus Smartsuite",
      "C. WordPerfect Office",
      "D. OpenOffice"]
     ),
    ("One disadvantage of software suites is that:",
     ["A. Users may be paying for features that they never use",
      "B. The packages take up a lot of disk space",
      "C. Upgrade costs are often expensive",
      "D. All of the choices are correct."]
     ),
    (
        "Which of the following, according to the text, are the basic components found in a comprehensive software suite?",
        ["A. Word processing, spreadsheet, and accounting",
         "B. Word processing, spreadsheet, and email",
         "C. Word processing, spreadsheet, database manager, and presentation graphics",
         "D. Word processing, database manager, presentation graphics, and email"]
    ),
    (
        "According to the text, the most important software component for many computer users today is the once simple and limited, but now powerful and feature rich, ___.",
        ["A. word processing application",
         "B. presentation graphics package",
         "C. web browser",
         "D. database management system"]
    ),
    ("According to the text, Web browsers are sometimes called the ___.",
     ["A. HTML client",
      "B. communication tool of the future",
      "C. universal client",
      "D. online collaboration client"]
     ),
    ("According to the text, which of the following is true of integrated packages?",
     ["A. They have more features than software suites",
      "B. They are more powerful than software suites",
      "C. They are cheaper than software suites",
      "D. They require more disk space than software suites"]
     ),
    ("According to the text, which of the following is not true of integrated packages?",
     ["A. They require less disk space than software suites",
      "B. They have fewer features than software suites",
      "C. They are more powerful than software suites",
      "D. They are cheaper than software suites"]
     ),
    ("According to the text, experts predict the Web browser will be the model for:",
     ["A. Internet development tools for the future",
      "B. How most people use networked computers in the future",
      "C. New graphical user interfaces in the future",
      "D. Cloud computing"]
     ),
    ("According to the text, e-mail:",
     ["A. Is a fad that will soon disappear",
      "B. Will be replaced by instant messaging",
      "C. Works best in cloud computing",
      "D. Has changed the way people work and communicate"]
     ),
    ("All of these statements regarding web logs or blogs are false except:",
     ["A. Blogs are websites of personal origin, not commercial.",
      "B. Each blog is a developing commentary on a particular theme that uses a dated log format.",
      "C. Blogs are declining in popularity because they are difficult to update.",
      "D. The information on a blog can only be written by the site owner."]
     ),
    ("All of the following are considered characteristics of a word processing package except:",
     ["A. Spell checker and thesaurus",
      "B. Grammar and punctuation correction",
      "C. Instant messaging",
      "D. Web page design capability"]
     ),
    ("All of the following are considered characteristics of a desktop publishing package except:",
     ["A. Used to print newsletters and brochures",
      "B. Imports text and graphic files from other programs",
      "C. Used for business analysis and modeling",
      "D. Used to print books and manuals"]
     ),
    ("According to the text, spreadsheet packages are used by virtually every business for ___.",
     ["A. analysis, planning, and modeling",
      "B. maintaining accounting records, such as a general ledger",
      "C. keeping up-to-the-minute inventory records",
      "D. tracking human resources"]
     ),
    ("When using a spreadsheet package to answer what if questions, the user must change:",
     ["A. Only a selected variable to see the impact of that change",
      "B. A number of variables to make a single change to the spreadsheet output",
      "C. All the formulas in order to calculate new values",
      "D. Nothing - spreadsheets cannot be used to answer what if questions"]
     ),
    (
        "Which one of the following would typically not be accomplished with presentation graphics software?",
        ["A. Converting numerical data into graphics and displays",
         "B. Incorporating multimedia files into presentations",
         "C. Preparing a computerized slideshow to accompany an oral presentation",
         "D. Preparing a text report for management"]
    ),
    ("Presentation graphics have become more powerful in recent years and can now:",
     ["A. Calculate formulas for business planning",
      "B. Enable collaboration within teams",
      "C. Organize appointments and calendars",
      "D. Prepare graphics and presentations for transfer to Web sites in HTML format"]
     ),
    ("Groupware aids collaboration by providing users with ___.",
     ["A. electronic mail, scheduling, and task management",
      "B. electronic mail and spreadsheet software",
      "C. electronic mail and word processing software",
      "D. All of the choices are correct."]
     ),
    ("Groupware is best described as a(n) ___ program.",
     ["A. general purpose application",
      "B. application specific",
      "C. system management",
      "D. system development"]
     ),
    ("Cloud computing is best described as:",
     ["A. Grid computing",
      "B. A style of computing where applications are provided by unknown sources hidden in the clouds",
      "C. A style of computing where resources are provided as a service over the Internet",
      "D. A style of computing where a network is not connected to the Internet"]
     ),
    ("Cloud computing is not:",
     ["A. Grid computing",
      "B. A style of computing users need not have knowledge, expertise, or control over the technological infrastructure",
      "C. A style of computing where resources are provided as a service over the Internet",
      "D. A metaphor for the Internet"]
     ),
    ("When a company purchases software, it has:",
     ["A. Purchased the rights of ownership",
      "B. Purchased a license to use the software under the terms of the agreement",
      "C. A difficult time obtaining a license because of legality issues",
      "D. None of the choices are correct."]
     ),
    ("System management programs:",
     [
         "A. Manage the hardware, software, networking, and data resources of computer systems during the execution of information processing jobs",
         "B. Manage e-mail and CASE tools for both end users and developers",
         "C. Help users develop information system programs and procedures",
         "D. All of the choices are correct."]
     ),
    (
        "Which of the following is a basic function that an operating system performs in the operation of a computer system?",
        ["A. User interface and support services",
         "B. Resource and task management",
         "C. File management and utilities",
         "D. It performs all of the functions above."]
    ),
    ("The user interface function of an operating system typically:",
     [
         "A. Allows end users to communicate with it so they can load programs, access files, and accomplish other tasks",
         "B. Manages the hardware resources of a computer system",
         "C. Controls the creation, deletion, and access of files of data and programs",
         "D. Manages the accomplishment of the computing tasks of end users"]
     ),
    ("Which of the following is the most popular type of user interface?",
     ["A. Graphical",
      "B. Command-driven",
      "C. Menu-driven",
      "D. Voice"]
     ),
    ("Which statement best describes open source software?",
     ["A. The primary enhancements are made by teenagers",
      "B. It is a very insecure operating system because of its huge security holes",
      "C. It is more reliable than traditional software because it is subject to more rigorous code review",
      "D. It is more costly than propriety software"]
     ),
    ("Open-source licensing is defined by all of the following except:",
     ["A. The license must not discriminate against any person or group of persons",
      "B. The license must not contaminate other software by placing restrictions on any software distributed along with the licensed software",
      "C. The license must allow modifications and derived works, and must allow them to be distributed under the same terms as the license of the original software",
      "D. The license must be specific to a product"]
     ),
    ("According to the text, Linux' popularity is due to all the following except:",
     ["A. Performance and price",
      "B. Flexibility and reliability",
      "C. It is Open Source software",
      "D. All of the choices are correct."]
     ),
    ("Machine languages are ___.",
     ["A. first-generation programming languages",
      "B. written using binary codes",
      "C. difficult languages in which to program compared to more recent languages",
      "D. All of the choices are correct."]
     ),
    (
        "The text outlines four levels of languages that allow a programmer to develop the sets of instructions that constitute a computer program. Which of the following is not one of those languages?",
        ["A. Machine languages",
         "B. Graphical languages",
         "C. Assembler languages",
         "D. High-level languages"]
    ),
    ("Which of the following characteristics does a high-level language possess?",
     ["A. They are also known as machine or assembler languages",
      "B. They are designed to be utilized by specific types of computers",
      "C. High-level instructions resemble mathematical expressions",
      "D. They are more efficient than assembler language programs"]
     ),
    ("Which of the following is not considered a high-level language?",
     ["A. BASIC",
      "B. COBOL",
      "C. FORTRAN",
      "D. Ruby on Rails"]
     ),
    (
        "Fifth generation languages, which are designed to be as much as possible like spoken languages, are referred to as ___ languages.",
        ["A. natural",
         "B. macro",
         "C. generator",
         "D. syntax"]
    ),
    ("Object-oriented programming languages:",
     ["A. Are a type of assembler language",
      "B. Separate data elements from the procedures that will be performed on them",
      "C. Use programming statements that tell objects to perform actions on themselves",
      "D. Are useful for numerical processing, but not for graphics-oriented applications"]
     ),
    ("___ is a major benefit of object-oriented programming.",
     ["A. Reusability of objects",
      "B. Conformity of objects",
      "C. A simplified programmer interface",
      "D. Faster compilation time"]
     ),
    (
        "All of the following are popular programming languages for developing multimedia web pages, websites, and web-based applications except:",
        ["A. XML",
         "B. HTML",
         "C. Java",
         "D. COBOL"]
    ),
    ("The acronym HTML stands for:",
     ["A. High Transfer Machine Language",
      "B. High Transmission Markup Language",
      "C. Hypertext Markup Language",
      "D. Hypermedia Markup Language"]
     ),
    ("Which of the following statements is applicable to the Java programming language?",
     ["A. It is a page description language that creates hypertext or hypermedia documents",
      "B. It inserts control codes within a document that create links to other parts of the document or to other documents anywhere on the World Wide Web",
      "C. It embeds control codes in the ASCII text of a document, which designates titles, headings, graphics, and multimedia components, as well as hyperlinks within the document",
      "D. It consists of small application programs called applets that can be executed by any computer and any operating system anywhere in a network"]
     ),
    (
        "Linux, an open source product, is a ___-like operating system that is rapidly gaining market share as a high-performance operating system for network and Web servers.",
        ["A. Unix",
         "B. BASIC",
         "C. COBOL",
         "D. Windows"]
    ),
    ("Program editors, debuggers, and code analyzers are types of ___.",
     ["A. Unix tools",
      "B. Programming languages",
      "C. CASE tools",
      "D. Operating Systems"]
     ),
    (
        "Those CASE tools that support activities early in the life cycle of a software project (e.g., requirements, design support tools) are sometimes called ___.",
        ["A. Pre-CASE tools",
         "B. Post-CASE tools",
         "C. Front-end or Upper CASE tools",
         "D. Back-end or Lower CASE tools"]
    ),
    (
        "Those CASE tools that are used later in the life cycle (e.g., compilers, test support tools) are sometimes called ___.",
        ["A. Pre-CASE tools",
         "B. Post-CASE tools",
         "C. Front-end or Upper CASE tools",
         "D. Back-end or Lower CASE tools"]
    ),
    (
        "In all information systems, data resources must be organized and structured in some logical manner, so that they can be:",
        ["A. Easily accessed",
         "B. Processed efficiently",
         "C. Retrieved quickly",
         "D. All of the choices are correct."]
    ),
    (
        "From a logical point of view, a(n) ___ is the smallest data element that can be observed and manipulated.",
        ["A. character",
         "B. bit",
         "C. attribute",
         "D. byte"]
    ),
    ("A record represents a collection of ___ that describe an entity.",
     ["A. characters",
      "B. fields",
      "C. files",
      "D. attributes"]
     ),
    ("All the fields used to describe the attributes of an entity are grouped to form a(n) ___.",
     ["A. field",
      "B. record",
      "C. file",
      "D. database"]
     ),
    ("A group of related records is a data file, or a ___.",
     ["A. field",
      "B. record",
      "C. table",
      "D. database"]
     ),
    ("Variable-length records contain:",
     ["A. both a variable number of fields and variable field lengths.",
      "B. both a variable number of fields and fixed field lengths.",
      "C. both a fixed number of fields and variable field lengths.",
      "D. both a fixed number of fields and fixed field lengths."]
     ),
    ("Fixed-length records contain:",
     ["A. both a variable number of fields and variable field lengths.",
      "B. both a variable number of fields and fixed field lengths.",
      "C. both a fixed number of fields and variable field lengths.",
      "D. both a fixed number of fields and fixed field lengths."]
     ),
    ("When independent of any other files related to it, a single table is referred to as a(n):",
     ["A. Independent file",
      "B. Flat file",
      "C. Hierarchical file",
      "D. Non-variable file"]
     ),
    ("A(n) ___ is an integrated collection of logically related data elements.",
     ["A. master file",
      "B. program base",
      "C. database",
      "D. integrated file"]
     ),
    ("Databases contain data elements that describe both entities and the ___ among entities.",
     ["A. relationships",
      "B. disparities",
      "C. subsets",
      "D. applications"]
     ),
    (
        "Database management packages based on the ___ model can link data elements from various tables to provide information to users.",
        ["A. object-oriented",
         "B. relational",
         "C. network",
         "D. hierarchical"]
    ),
    (
        "Early mainframe DBMS packages used the ___ structure, in which all records are dependent and arranged in multilevel structures, consisting of one root record and any number of subordinate levels.",
        ["A. network",
         "B. relational",
         "C. hierarchical",
         "D. object-oriented"]
    ),
    (
        "In a(n) ___ database structure, all of the relationships among records are one-to-many, because each data element is related to only one element above it.",
        ["A. hierarchical",
         "B. relational",
         "C. network",
         "D. object-oriented"]
    ),
    (
        "Which database model allows many-to-many relationships among records so that a data element can be accessed by following one of several paths?",
        ["A. Hierarchical",
         "B. Network",
         "C. Object-oriented",
         "D. Relational"]
    ),
    ("The ___ model is the most widely used database structure today.",
     ["A. network",
      "B. object-oriented",
      "C. relational",
      "D. hierarchical"]
     ),
    (
        "In the relational database model, all data elements within the database are viewed as being stored in the form of simple two-dimensional tables, sometimes referred to as ___.",
        ["A. records",
         "B. rows",
         "C. columns",
         "D. relations"]
    ),
    (
        "The tables in a relational database are flat files which have rows and columns. Each row represents a ___ in the file.",
        ["A. field",
         "B. record",
         "C. file",
         "D. relation"]
    ),
    (
        "The tables in a relational database are flat files which have rows and columns. Each column represents a ___ in the file.",
        ["A. field",
         "B. record",
         "C. file",
         "D. relation"]
    ),
    (
        "The ___ operation is used to create a subset of the columns contained in the temporary tables created by the select and join operations.",
        ["A. link",
         "B. relate",
         "C. project",
         "D. merge"]
    ),
    (
        "Using a relational database, a user can temporarily combine two or more tables so that he/she can see relevant data in a form that looks like it is in one big table. This is the ___ operation.",
        ["A. join",
         "B. link",
         "C. merge",
         "D. select"]
    ),
    ("___ is the most commonly used database application for the PC.",
     ["A. Oracle 10g",
      "B. Microsoft Access",
      "C. DB2",
      "D. SQL Server"]
     ),
    (
        "___ databases have become the most popular structure for analytical databases that support online analytical process (OLAP) applications, in which fast answers to complex queries are expected.",
        ["A. Relational",
         "B. Object-oriented",
         "C. Inter-relational",
         "D. Multidimensional"]
    ),
    (
        "The ___ database structure is considered one of the key technologies of a new generation of Web-based applications.",
        ["A. hierarchical",
         "B. relational",
         "C. object-oriented",
         "D. multidimensional"]
    ),
    (
        "The object-oriented database model supports ___. That is, new objects can be automatically created by replicating some or all of the characteristics of one or more parent objects.",
        ["A. inheritance",
         "B. morphing",
         "C. duplication",
         "D. cloning"]
    ),
    ("Object technology allows designers to do all of the following except:",
     ["A. Develop product designs",
      "B. Replicate product designs and then modify them to create new product designs",
      "C. Save designs as objects in an object-oriented database",
      "D. Substantially reduce the file size of designs"]
     ),
    (
        "Which database structure works effectively with complex data types, such as video clips, audio segments, and other subsets of Web pages, and is considered one of the key technologies of Web-based applications?",
        ["A. Hierarchical",
         "B. Network",
         "C. Object-oriented",
         "D. Relational"]
    ),
    ("A database with a(n) ___ data structure can easily handle a many-to-many data relationship.",
     ["A. hierarchical",
      "B. network",
      "C. relational",
      "D. object-oriented"]
     ),
    ("A database with a(n) ___ data structure can easily handle ad hoc requests for information.",
     ["A. hierarchical",
      "B. network",
      "C. relational",
      "D. object-oriented"]
     ),
    (
        "According to one database pioneer, the future development of databases and data warehouses will depend on ___.",
        ["A. rows",
         "B. columns",
         "C. transaction",
         "D. All of the choices are correct."]
    ),
    (
        "Large organizations usually place control of enterprise-wide database development in the hands of ___.",
        ["A. Database administrators (DBAs)",
         "B. Automated CASE tools",
         "C. End users",
         "D. All of the choices are correct."]
    ),
    ("According to the text, most data warehouses will run ___ in a column format.",
     ["A. 20 times faster",
      "B. 50 times faster",
      "C. 50 times slower",
      "D. None of the choices are correct."]
     ),
    (
        "Database administrators and database design analysts work with end users and systems analysts to do all of the following except:",
        ["A. Model business processes and the data they require",
         "B. Determine what data definitions should be included in the database",
         "C. Determine what structure or relationships should exist among the data elements",
         "D. Enter live data into the system until it has proven to be reliable"]
    ),
    ("___ are used to model the relationships among the many entities involved in business processes.",
     ["A. Entity-relationship diagrams",
      "B. Data-flow diagrams",
      "C. Schema diagrams",
      "D. Subschema diagrams"]
     ),
    ("The physical design stage of database development:",
     ["A. Develops a model of business processes",
      "B. Translates conceptual models into the data models",
      "C. Determines the data storage structures and access methods",
      "D. Defines the information needs of end users in a business process"]
     ),
    (
        "The ___ stage of database development translates the conceptual models into the data model of a DBMS.",
        ["A. data planning",
         "B. requirements specification",
         "C. conceptual design",
         "D. logical design"]
    ),
    ("A ___ is an overall logical view of the relationships among the data elements in a database.",
     ["A. schema",
      "B. subschema",
      "C. logical data model",
      "D. conceptual design"]
     ),
    (
        "A ___ is an overall logical view of the relationships needed to support specific end-user application programs that will access the database.",
        ["A. schema",
         "B. subschema",
         "C. logical data model",
         "D. conceptual design"]
    ),
    ("According to the textbook case, the innovation of the open-source product Hadoop is ___.",
     ["A. that it has not been sued by Google",
      "B. that it actually works",
      "C. that it has no proprietary predecessor",
      "D. its algorithms run contrary to contemporary mathematics"]
     ),
    (
        "According to the textbook case, file processing in Hadoop is not halted by hardware failures because ___.",
        ["A. Hadoop is a software product",
         "B. Open-source products are not affected by hardware failures",
         "C. Hadoop is an Internet product and does not need hardware",
         "D. Hadoop keeps three (3) copies of all data"]
    ),
    (
        "Operational databases store the detailed data needed to support the business processes and operations of a company. They are also called ___.",
        ["A. Subject area databases",
         "B. Transaction databases",
         "C. Production databases",
         "D. All of the choices are correct."]
    ),
    ("The primary challenge of a distributed database is:",
     ["A. Data accuracy",
      "B. Data transmission speed",
      "C. Storage costs",
      "D. Data security"]
     ),
    (
        "Which of the following statements concerning the replication and duplication process for updating distributed databases is correct?",
        ["A. The two terms are interchangeable because the processes work the same way",
         "B. Duplication is the more complicated process because it has to identify one database as a master and prevent changes being made to any database other than the master",
         "C. Replication is the more complicated process because it must find changes in each distributed database and make appropriate changes to make each database identical",
         "D. None of the choices are correct."]
    ),
    (
        "What type of databases are employees using when they access online data banks, whether those data banks are free or paid for through subscriptions?",
        ["A. Common databases",
         "B. Distributed databases",
         "C. External databases",
         "D. Local databases"]
    ),
    (
        "A central source of data that have been cleaned, transformed, and cataloged so that they can be used for business analysis, market research, and decision support is called a ___.",
        ["A. data mart",
         "B. data warehouse",
         "C. transaction processing mart",
         "D. data repository"]
    ),
    ("A data warehouse contains data that have been processed in all the following ways except:",
     ["A. Separated",
      "B. Cleaned",
      "C. Transformed",
      "D. Cataloged"]
     ),
    ("Which of the following is true of data marts?",
     ["A. They hold data from many different data warehouses.",
      "B. They are a subset of a data warehouse.",
      "C. They focus on many generalized aspects of a company.",
      "D. None of the choices are correct."]
     ),
    ("Which of the following is true of data in a data warehouse?",
     ["A. Data in operational databases is ever changing; data in data warehouses is static",
      "B. Data in operational databases is static; data in data warehouses is ever changing",
      "C. Data in operational databases can be cataloged; data in data warehouses cannot",
      "D. None of the choices are correct."]
     ),
    ("Which of the following is a legitimate use for data mining?",
     ["A. Performing market - basket analysis to identify new product bundles",
      "B. Profiling customers",
      "C. Finding the root cause of a quality or manufacturing problem",
      "D. All of the choices are correct."]
     ),
    ("All of the following contribute to problems when using a file management approach except:",
     ["A. Data redundancy",
      "B. Lack of integration of data",
      "C. Data independence",
      "D. Lack of data integrity"]
     ),
    (
        "Database management involves the use of database management software to control how databases are ___.",
        ["A. created",
         "B. interrogated",
         "C. maintained",
         "D. All of the choices are correct."]
    ),
    (
        "In mainframe and server computer systems, the database management system controls the ___ of the databases of computer-using organizations.",
        ["A. maintenance",
         "B. development",
         "C. use",
         "D. All of the choices are correct."]
    ),
    ("All of the following are major functions of a database management system except:",
     ["A. Creating new databases and database applications",
      "B. Identifying insufficient data processing or storage needs",
      "C. Maintaining the quality of the data in an organization's databases",
      "D. Using the databases of an organization to provide the information needed by its end users"]
     ),
    (
        "Database development involves defining and organizing the ___ of the data needed to build a database.",
        ["A. structure",
         "B. content",
         "C. relationships",
         "D. All of the choices are correct."]
    ),
    ("A DBMS query language is designed to:",
     ["A. Support information systems professionals in the development of complex application software",
      "B. Support end users who wish to obtain ad hoc reports",
      "C. Provide efficient batch mode processing of the database",
      "D. Specify the content, relationships, and structure of a database"]
     ),
    ("The database maintenance process is accomplished via:",
     ["A. Hierarchical database systems that provide flexibility and network databases",
      "B. Transaction processing systems and other end user applications, with the support of the DBMS",
      "C. Graphical query languages correctly phrasing SQL",
      "D. File processing systems with the support of 4GLs"]
     ),
    ("The basic form of a SQL query is:",
     ["A. SELECT … AND … OR",
      "B. SELECT … WHERE … FROM …",
      "C. SELECT … FROM … WHERE …",
      "D. AND … OR … NOT …"]
     ),
    ("Boolean logic deals with three logical operators:",
     ["A. AND, OR, and BUT",
      "B. AND, NOT, and BUT",
      "C. OR, BUT, and NOT",
      "D. AND, OR, and NOT"]
     ),
    (
        "Many end users have trouble correctly phrasing database language search queries, so most end-user DBMS packages now offer ___ methods.",
        ["A. speech recognition",
         "B. command line",
         "C. GUI",
         "D. All of the choices are correct."]
    ),
    ("Telecommunications and network technologies are internetworking and revolutionizing ___.",
     ["A. business and society",
      "B. business and globalization",
      "C. society and politics",
      "D. globalization and politics"]
     ),
    ("Which of the following statements best defines a network?",
     ["A. The usefulness or utility that comes from linking computers together",
      "B. An interrelated or interconnected chain, group, or system",
      "C. Computers linked together via cabling or wireless technology",
      "D. A group of individuals linked via hardware and software"]
     ),
    (
        "A network with 100 nodes has 9,900 possible connections. A network with 1,000 nodes has ___ possible connections.",
        ["A. 9,900,000",
         "B. 999,000",
         "C. 99,000",
         "D. over one million"]
    ),
    ("Metcalfe's law states that:",
     ["A. The usefulness or utility of a network equals the square of the number of users",
      "B. More network nodes equals more usefulness to network members",
      "C. Networks with too many nodes rapidly lose their effectiveness",
      "D. The usefulness or utility of a network equals the number of users times the number of nodes"]
     ),
    ("A change in technology induces social, political, and economic system changes ___.",
     ["A. long before a critical mass of users is reached.",
      "B. before the technology is well understood.",
      "C. only after a critical mass of users is reached.",
      "D. when it is used as a political tool by radical countries."]
     ),
    ("The telecommunications industry has changed ___.",
     ["A. from a deregulated market to government-regulated monopolies.",
      "B. not at all since 1900.",
      "C. from government-regulated monopolies to a deregulated market.",
      "D. none of the above."]
     ),
    ("Open systems are a recent telecommunications trend. Open systems:",
     ["A. Use common standards for hardware, software, applications, and networking",
      "B. Create a computing environment that is easily accessed by end users and their networked computer systems",
      "C. Provide greater connectivity, and a high degree of network interoperability",
      "D. All of the choices are correct."]
     ),
    (
        "Programming that serves to glue together or mediate between two separate, and usually already existing, programs is known as ___.",
        ["A. front-line software",
         "B. software handshaking",
         "C. middleware",
         "D. back-line software"]
    ),
    (
        "Local and global telecommunications networks are rapidly converting to digital transmission technologies. Digital technology provides all of the following benefits over analog technology except:",
        ["A. Much lower error rates",
         "B. Equivalent transmission speeds",
         "C. Movement of larger amounts of information",
         "D. Greater economy"]
    ),
    ("Telecommunications networks now play vital and pervasive roles in Web-enabled ___.",
     ["A. e-business processes",
      "B. electronic commerce",
      "C. enterprise collaboration",
      "D. All of the choices are correct."]
     ),
    ("Which of the following statements regarding Internet2 is true?",
     ["A. Internet2, like the first Internet, is open to all users",
      "B. Internet2 uses the same infrastructure as the current Internet, so it will be easy to learn",
      "C. The purpose of Internet2 is to build a roadmap that can be followed during the next stage of innovation for the current Internet",
      "D. Internet2 will someday replace the original Internet"]
     ),
    (
        "Most of the institutions and commercial partners on the Internet2 network are connected via ___, a network backbone that will soon support throughput of 10 Gbps.",
        ["A. Abilene",
         "B. Phoenix",
         "C. Enterprise",
         "D. Indiana"]
    ),
    (
        "Traveling salespeople and those at regional sales offices can use the Internet, extranets, and other networks to transmit customer orders from their laptop or desktop PCs, thus breaking ___ barriers.",
        ["A. physical",
         "B. competition",
         "C. structural",
         "D. geographic"]
    ),
    (
        "Telecommunications-based business applications can help a company overcome all of the following barriers to business success except:",
        ["A. Time barriers",
         "B. Geographic barriers",
         "C. Human resource barriers",
         "D. Cost barriers"]
    ),
    ("All of the following statements about the Internet revolution are true except:",
     [
         "A. The Internet has become the largest and most important network today, and has evolved into a global information superhighway",
         "B. The central computer system of the Internet is the most powerful communications center in the world",
         "C. The Internet is constantly expanding, as more and more businesses and other organizations join its global web",
         "D. The Internet does not have a headquarters or governing body"]
     ),
    ("Which of the following statements regarding Internet Service Providers is correct?",
     ["A. ISPs provide individuals and organizations with access to the Internet for a fee",
      "B. ISPs are independent organizations; they have no connection to one another",
      "C. ISPs are no longer necessary for access to the Internet",
      "D. ISPs provide a direct connection between a company's networks and the Internet"]
     ),
    ("ISPs are connected to one another through network ___.",
     ["A. touch points",
      "B. portals",
      "C. access points",
      "D. hubs"]
     ),
    ("Which of the following is a key business use of the Internet?",
     ["A. Internet websites for interactive marketing and electronic commerce",
      "B. E-mail, file transfer, and discussion forums",
      "C. Intranet links with remote employee sites",
      "D. All of the choices are correct."]
     ),
    (
        "Applications that use the Internet and Internet-based technologies are typically less expensive to ___ than traditional systems.",
        ["A. develop",
         "B. operate",
         "C. maintain",
         "D. All of the choices are correct."]
    ),
    (
        "Most companies are building e-business and e-commerce websites to achieve all of the following goals except:",
        ["A. Generate new revenue from online sales",
         "B. Increase foot traffic at brick and mortar locations",
         "C. Reduce transaction costs",
         "D. Increase the loyalty of existing customers via Web customer service and support"]
    ),
    (
        "An ___ is a network inside an organization that uses Internet technologies to provide an Internet-like environment within the enterprise.",
        ["A. extranet",
         "B. omninet",
         "C. intranet",
         "D. none of the above"]
    ),
    (
        "An ___ is a network link that uses Internet technologies to interconnect the intranet of a business with the intranets of its customers, suppliers, or other business partners.",
        ["A. extranet",
         "B. omninet",
         "C. intranet",
         "D. none of the above"]
    ),
    ("The use of an intranet in an organization ___.",
     ["A. can significantly improve communications and collaboration within an enterprise.",
      "B. can significantly hinder communications and collaboration within an enterprise.",
      "C. has no effect communications and collaboration within an enterprise.",
      "D. is only possible if the organization is using WiFi."]
     ),
    (
        "All of the following would typically be supported by an organization's intranet information portal except:",
        ["A. Communication and collaboration",
         "B. Business operations and management",
         "C. Web publishing",
         "D. Recruitment"]
    ),
    (
        "The comparative ___ of publishing and accessing multimedia business information internally via intranet websites has been one of the primary reasons for the explosive growth in the use of intranets in business.",
        ["A. attractiveness",
         "B. lower cost",
         "C. ease",
         "D. All of the choices are correct."]
    ),
    (
        "Based on the information presented in the text, telecommunications terminals are best described as:",
        [
            "A. Any input/output device that uses telecommunications networks to transmit or receive data, including telephones",
            "B. Devices that support data transmission and reception between terminals and computers",
            "C. Channels over which data are transmitted and received",
            "D. Programs that control telecommunications activities and manage the functions of telecommunications networks"]
    ),
    (
        "The text lists five basic categories of components in a telecommunications network. One of these categories includes telecommunications processors, which:",
        ["A. Support data transmission and reception between terminals and computers",
         "B. Are channels over which data are transmitted and received",
         "C. Consist of programs that control telecommunications activities and manage the functions of telecommunications networks",
         "D. Include input/output terminals"]
    ),
    ("The five basic categories of components in a telecommunications network include:",
     [
         "A. Protocols, telecommunications channels, computers, telecommunications control software, and modems",
         "B. Terminals, telecommunications processors, telecommunications channels, computers, and telecommunications control software",
         "C. Terminals, telecommunications channels, computers, and modems",
         "D. Terminals, telecommunications processors, computers, modems, and protocols"]
     ),
    (
        "A network that covers a large geographic distance, such as a state or a country, is considered a ___ network.",
        ["A. client/server",
         "B. local area",
         "C. small area",
         "D. wide area"]
    ),
    ("Which of the following best describes a local area network?",
     ["A. A network that covers a large geographic area, such as a city or state",
      "B. A network that connects computers within a limited physical area, such as inside a single building",
      "C. A network that covers no more than a single state",
      "D. A private network that uses the Internet as its main backbone"]
     ),
    ("To communicate over a network, each PC usually has a circuit board called a ___.",
     ["A. printed circuit card",
      "B. modem",
      "C. router",
      "D. network interface card"]
     ),
    ("All of the following statements about a virtual private network are correct except:",
     ["A. Uses the Internet as its main backbone network",
      "B. Connects the intranets of a company's different locations, or establishes extranet links between a company and its customers, suppliers, and business partners",
      "C. Relies on modem, twisted-pair wire, and router technology",
      "D. Relies on network firewalls, encryption, and other security features to provide a secure network"]
     ),
    ("All the following describe a VPN except:",
     ["A. A VPN uses the Internet as its main backbone network.",
      "B. A VPN relies on network firewalls, encryption, and other Internet and intranet security features.",
      "C. A VPN uses the Internet to establish secure intranets between its distant offices and locations.",
      "D. A VPN is available for use by anyone with access to the Internet."]
     ),
    ("Older, traditional mainframe-based business information systems are called ___ systems.",
     ["A. historical",
      "B. standard",
      "C. legacy",
      "D. application"]
     ),
    ("Most Linux distributions are released via BitTorrent to help with ___ needs.",
     ["A. security",
      "B. bandwidth",
      "C. user registration",
      "D. file compression"]
     ),
    ("The Internet, as originally conceived in the late 1960's was a ___ system.",
     ["A. client-server",
      "B. central server",
      "C. pure peer-to-peer",
      "D. peer-to-peer"]
     ),
    ("In telecommunications networks, twisted-pair wire:",
     ["A. Is the least commonly used medium",
      "B. Facilitates mobile data communication",
      "C. Is used for both voice and data transmission",
      "D. Is commonly laid on the floors of lakes and oceans"]
     ),
    (
        "A communications medium that consists of one or more central wires surrounded by thick insulation is called ___ cable.",
        ["A. coaxial",
         "B. fiber optic",
         "C. twisted-pair",
         "D. packet-transmission"]
    ),
    ("Compared to coaxial cable, standard twisted-pair telephone lines:",
     ["A. Support lower data transmission speeds",
      "B. Are virtually the same as coaxial cable in speed and service provided",
      "C. Have less interference and distortion because of their insulation",
      "D. None of the choices are correct."]
     ),
    (
        "Fiber optics uses cables consisting of one or more hair-thin filaments of ___ fiber wrapped in a protective jacket.",
        ["A. glass",
         "B. plastic",
         "C. ceramic",
         "D. nylon"]
    ),
    ("Fiber optics are regarded as the communications media of the future, primarily due to its ___.",
     ["A. availability",
      "B. greater speed and capacity",
      "C. lower installation costs",
      "D. greater compatibility with existing communications media"]
     ),
    ("As it relates to telecommunications media, the problem of the last mile is:",
     ["A. A low voltage drop at the end of the line",
      "B. Tying into older technology",
      "C. Finding the money to complete the project",
      "D. None of the choices are correct."]
     ),
    ("Which of the following technologies transmits data at the fastest rate?",
     ["A. Modem",
      "B. Cable modem",
      "C. ISDN",
      "D. Home satellite"]
     ),
    ("An internetworking unit that connects networks based on different protocols is a ___.",
     ["A. bridge",
      "B. router",
      "C. gateway",
      "D. hub"]
     ),
    ("In a telecommunications network, a hub is a communications processor that:",
     ["A. Connects two LANS based on the same network standards or protocols",
      "B. Connects different communications architectures",
      "C. Facilitates port switching",
      "D. None of the choices are correct."]
     ),
    ("In a telecommunications network, a gateway is a communications processor that:",
     ["A. Is used for port switching",
      "B. Connects different communications architectures",
      "C. Connects two LANS based on the same network standards or protocols",
      "D. Connects LANs to Wi-Fi networks"]
     ),
    ("In telecommunications networks, multiplexers:",
     ["A. Convert digital signals to analog and vice versa",
      "B. Allow a single communications channel to carry multiple simultaneous data transmissions",
      "C. Include bridges, routers, hubs, and gateways, which interconnect a local area network with other local and wide area networks",
      "D. Make connections between communications circuits in a network"]
     ),
    ("Network management package functions include all of the following except:",
     ["A. Managing network resources and traffic to avoid congestion",
      "B. Providing security",
      "C. Informing network administrators of potential problems before they occur",
      "D. All of the choices are functions of network management packages."]
     ),
    (
        "Security is a top concern of network management today, so telecommunications software must provide all of the following except:",
        ["A. Authentication",
         "B. Encryption",
         "C. Firewalls",
         "D. Central processing"]
    ),
    (
        "A network configuration that consists of a central computer system with a number of smaller computers tied directly to it, but not to each other, is a ___ network.",
        ["A. bus",
         "B. ring",
         "C. central processing",
         "D. star"]
    ),
    ("Which of the following best describes how star, ring, and bus networks differ?",
     ["A. Performance and reliability",
      "B. Performance, reliability, and cost",
      "C. Reliability and cost",
      "D. Performance and cost"]
     ),
    (
        "A(n) ___ is a standard set of rules and procedures for the control of communication in a network.",
        ["A. amplification",
         "B. algorithm",
         "C. protocols",
         "D. transponders"]
    ),
    ("Which one of the following statements regarding a telecommunications network is false?",
     [
         "A. A protocol is a standard set of rules and procedures for the control of communications in a network",
         "B. The communications control information needed for handshaking between terminals and computers is a protocol",
         "C. A protocol deals with the control of data transmission/reception in a network",
         "D. Protocols are not applicable to hardware, such as cables and modems"]
     ),
    ("The ___ layer in an OSI model provides communications services for end users.",
     ["A. application",
      "B. data link",
      "C. network",
      "D. transport"]
     ),
    ("In an OSI model, the ___ layer does the routing and forwarding.",
     ["A. physical",
      "B. data link",
      "C. network",
      "D. application"]
     ),
    (
        "When IP was first standardized, the specification required that each system attached to the Internet be assigned a unique, ___ Internet address value.",
        ["A. 4-bit",
         "B. 8-bit",
         "C. 16-bit",
         "D. 32-bit"]
    ),
    ("All of the following statements regarding Internet telephony are correct except:",
     ["A. It is often referred to as voice over IP or VOIP",
      "B. It involves using an Internet connection to pass voice data using IP instead of a standard public telephone network",
      "C. It incurs standard long-distance telephone call charges",
      "D. It demands a very well-configured network to run smoothly"]
     ),
    (
        "Communications channels such as microwave, fiber optics, or satellite transmission that provide high-speed transmission rates typically use ___ channels.",
        ["A. broadband",
         "B. narrow-band",
         "C. wireless",
         "D. voice-band"]
    ),
    ("ATM (asynchronous transfer mode) is an emerging high-capacity ___ switching technology.",
     ["A. node",
      "B. packet",
      "C. cell",
      "D. network"]
     ),
    (
        "VoIP works by digitizing a voice signal, chopping it into ___, and then sending them over a company's computer network or the Internet, much like data or email.",
        ["A. bits",
         "B. packets",
         "C. characters",
         "D. waves"]
    ),
    ("IPv4, the current Internet addressing protocol, can accommodate about ___ addresses.",
     ["A. 4 trillion",
      "B. 4 billion",
      "C. 4 million",
      "D. None of the above"]
     ),
    (
        "___ is defined as the use of the Internet and other networks and information technologies to support electronic commerce, enterprise communication and collaboration, and Web-enabled business processes, both within a networked enterprise and with customers and business partners.",
        ["A. Electronic business",
         "B. Enterprise collaboration",
         "C. Cross-functional system management",
         "D. Supply chain management"]
    ),
    (
        "___ systems cross the boundaries of traditional business functions in order to reengineer and improve vital business processes all across the enterprise.",
        ["A. Electronic business",
         "B. Enterprise collaboration",
         "C. Cross-functional enterprise",
         "D. Supply chain management"]
    ),
    (
        "Networked enterprises view ___ systems as a strategic way to use IT to share information resources and improve the efficiency and effectiveness of business processes.",
        ["A. electronic business",
         "B. enterprise collaboration",
         "C. cross-functional enterprise",
         "D. supply chain management"]
    ),
    (
        "Moving from mainframe-based legacy systems to integrated, cross-functional client/server applications typically involves installing ___ software.",
        ["A. enterprise resource planning",
         "B. supply chain management",
         "C. customer relationship management",
         "D. all of the choices are correct."]
    ),
    (
        "Instead of focusing on the information processing requirements of business functions, enterprise software focuses on supporting integrated clusters of ___ involved in the operations of a business.",
        ["A. application software",
         "B. business processes",
         "C. customer relationships",
         "D. all of the choices are correct."]
    ),
    (
        "A(n) ___ architecture illustrates the inter-relationships of the major cross-functional enterprise applications that many companies have, or are installing, today.",
        ["A. enterprise application",
         "B. enterprise operation",
         "C. cross-functional",
         "D. none of the choices are correct."]
    ),
    (
        "Which of the following applications focuses on the efficiency of a firm's internal production, distribution, and financial processes?",
        ["A. Customer relationship management",
         "B. Enterprise resource planning",
         "C. Knowledge management",
         "D. Supply chain management"]
    ),
    (
        "Which of the following applications focuses on acquiring and retaining profitable customers via marketing, sales, and service processes?",
        ["A. Customer relationship management",
         "B. Enterprise resource planning",
         "C. Knowledge management",
         "D. Supply chain management"]
    ),
    (
        "Which of the following applications focuses on developing the most efficient and effective sourcing and procurement processes?",
        ["A. Customer relationship management",
         "B. Enterprise resource planning",
         "C. Knowledge management",
         "D. Supply chain management"]
    ),
    (
        "Which of the following applications focuses on tools that support group collaboration and decision support?",
        ["A. Customer relationship management",
         "B. Enterprise resource planning",
         "C. Knowledge management",
         "D. Supply chain management"]
    ),
    (
        "Which of the following applications aims to acquire and retain partners who can enhance the sale and distribution of a firm's products and services?",
        ["A. Customer relationship management",
         "B. Enterprise resource planning",
         "C. Partner Relationship Management",
         "D. Supply chain management"]
    ),
    ("As described in the text, partner relationship management focuses on:",
     ["A. Developing the most efficient and effective sourcing and procurement processes",
      "B. Acquiring and retaining profitable customers via delivery of timely products",
      "C. Acquiring and retaining partners who can enhance the selling and distribution of a firm's products and services",
      "D. Providing a firm's employees with tools that support group collaboration and decision support"]
     ),
    ("As described in the text, supply chain management focuses on:",
     ["A. Developing the most efficient and effective sourcing and procurement processes",
      "B. Acquiring and retaining profitable customers via delivery of timely products",
      "C. Acquiring and retaining partners who can enhance the selling and distribution of a firm's products and services",
      "D. Providing a firm's employees with tools that support group collaboration and decision support"]
     ),
    ("According to the text, customer relationship management focuses on:",
     ["A. Developing the most efficient and effective sourcing and procurement processes",
      "B. Acquiring and retaining profitable customers via marketing and delivery of timely products and services",
      "C. Acquiring and retaining partners who can enhance the selling and distribution of a firm's products and services",
      "D. Providing a firm's employees with tools that support group collaboration and decision support"]
     ),
    ("According to the text, enterprise resource planning focuses on:",
     ["A. Developing the most efficient and effective sourcing and procurement processes",
      "B. Acquiring and retaining profitable customers via delivery of timely products",
      "C. The efficiency of a firm's internal production, distribution, and financial processes",
      "D. Providing a firm's employees with tools that support group collaboration and decision support"]
     ),
    ("As described in the text, knowledge management focuses on:",
     ["A. Developing the most efficient and effective sourcing and procurement processes",
      "B. Acquiring and retaining profitable customers via delivery of timely products",
      "C. Acquiring and retaining partners who can enhance the selling and distribution of a firm's products and services",
      "D. Providing a firm's employees with tools that support group collaboration and decision support"]
     ),
    (
        "Enterprise application integration (EAI) software enables users to model the business processes and interactions that should occur between:",
        ["A. International divisions",
         "B. Suppliers and customers",
         "C. End users",
         "D. Business applications"]
    ),
    (
        "Enterprise application integration (EAI) software provides ___ that performs data conversion and subordination, and application communication and messaging services.",
        ["A. middleware",
         "B. a legacy system",
         "C. the telecommunication protocol",
         "D. a business application"]
    ),
    ("Distribution and manufacturing are ___.",
     ["A. middleware",
      "B. legacy systems",
      "C. back office systems",
      "D. front office systems"]
     ),
    (
        "___ software can integrate the front-office and back office systems applications of a business so they work together in a seamless, integrated way.",
        ["A. Customer relationship management (CRM)",
         "B. Knowledge management (KM)",
         "C. Enterprise application integration (EAI)",
         "D. Supply chain management (SCM)"]
    ),
    ("Customer service and sales order entry are ___.",
     ["A. middleware",
      "B. legacy systems",
      "C. back office systems",
      "D. front office systems"]
     ),
    (
        "___ are events that occur as part of doing business, such as sales, purchases, deposits, withdrawals, refunds, and payments.",
        ["A. Items",
         "B. Transactions",
         "C. Occurrences",
         "D. Processes"]
    ),
    ("A transaction is ___.",
     ["A. any exchange of goods",
      "B. any business event that must be captured and recorded",
      "C. an event requiring an exchange of money",
      "D. any business process where an exchange of resources occurs"]
     ),
    (
        "Transaction processing systems play a vital role in supporting the ___ of an e-business enterprise.",
        ["A. customer service",
         "B. product distribution",
         "C. operations",
         "D. systems architecture"]
    ),
    (
        "Transaction processing systems are ___ information systems that process data resulting from the occurrence of business transactions.",
        ["A. customer relationship management (CRM)",
         "B. knowledge management (KM)",
         "C. operational accounting",
         "D. cross-functional"]
    ),
    (
        "Online transaction processing is considered a ___ system because it captures and processes transactions immediately.",
        ["A. customer service",
         "B. post-event",
         "C. batch processing",
         "D. real time"]
    ),
    ("The first step of the transaction processing cycle is ___.",
     ["A. inquiry processing",
      "B. document generation",
      "C. transaction processing",
      "D. data entry"]
     ),
    (
        "___ update the corporate databases of an organization to reflect changes resulting from day-to-day business transactions.",
        ["A. Online transaction processing (OLTP) systems",
         "B. Enterprise application integration systems",
         "C. Accounting processing systems",
         "D. Transaction processing systems"]
    ),
    ("Transaction processing systems process data in two basic ways: ___ and ___.",
     ["A. Online processing, offline processing",
      "B. Online/real-time processing, batch processing",
      "C. Distributed processing, centralized processing",
      "D. Replicated processing, distributed processing"]
     ),
    (
        "___ systems are cross-functional information systems that enhance communication and coordination among the members of business teams and workgroups.",
        ["A. Enterprise coordination",
         "B. Enterprise integration",
         "C. Enterprise collaboration",
         "D. Transaction processing"]
    ),
    (
        "The capabilities and potential of ___ are driving the demand for better enterprise collaboration tools in business.",
        ["A. the Internet",
         "B. intranets",
         "C. extranets",
         "D. All of the choices are correct."]
    ),
    (
        "Electronic mail, voice mail, faxing, Web publishing, bulletin board systems, and paging are considered ___ tools.",
        ["A. electronic communication",
         "B. collaborative work management",
         "C. electronic conferencing",
         "D. All of the choices are correct."]
    ),
    ("Video-conferencing, chat systems, and discussion forums are considered ___ tools.",
     ["A. electronic communication",
      "B. collaborative work management",
      "C. electronic conferencing",
      "D. All of the choices are correct."]
     ),
    ("Workflow systems, document sharing, and knowledge management are considered ___ tools.",
     ["A. electronic communication",
      "B. collaborative work management",
      "C. electronic conferencing",
      "D. All of the choices are correct."]
     ),
    ("Which of the following is considered a collaborative work management tool?",
     ["A. Calendaring and scheduling",
      "B. Instant messaging",
      "C. Voice conferencing",
      "D. Paging"]
     ),
    ("Which of the following is considered an electronic communications tool?",
     ["A. Calendaring and scheduling",
      "B. Instant messaging",
      "C. Voice conferencing",
      "D. Chat systems"]
     ),
    ("Which of the following is considered an electronic conferencing tool?",
     ["A. Calendaring and scheduling",
      "B. Instant messaging",
      "C. Data conferencing",
      "D. Paging"]
     ),
    ("Training in a virtual world is effective, but obstacles include both ___.",
     ["A. technology and culture",
      "B. hardware and software",
      "C. front office and back office",
      "D. suppliers and customers"]
     ),
    ("Training in a virtual world can both ___.",
     ["A. increase costs and increase efficiency",
      "B. lower costs and lower efficiency",
      "C. increase costs and lower efficiency",
      "D. lower costs and increase efficiency"]
     ),
    ("___ tools help people accomplish or manage group work activities.",
     ["A. Calendaring and scheduling",
      "B. Task and project management",
      "C. Collaborative work management",
      "D. Knowledge management"]
     ),
    ("Collaborative work management tools include all of the following except:",
     ["A. Calendaring and scheduling tools",
      "B. Task and project management",
      "C. Faxing, paging, and bulletin board systems",
      "D. Knowledge management"]
     ),
    (
        "A(n) ___ business system is a type of information system that supports the business functions of accounting, finance, marketing, operations management, and human resource management.",
        ["A. functional",
         "B. inter-enterprise",
         "C. collaboration",
         "D. enterprise resource"]
    ),
    ("Marketing information systems can help marketing managers with:",
     ["A. Customer relationship management",
      "B. Product planning and pricing",
      "C. Targeted marketing strategies",
      "D. All of the choices are correct."]
     ),
    ("Which of the following is considered a human resource business function?",
     ["A. Compensation analysis",
      "B. Payroll",
      "C. Customer relationship management",
      "D. Sales force automation"]
     ),
    ("Which of the following is considered a production/operations business function?",
     ["A. Personnel requirements forecasting",
      "B. Process control",
      "C. Investment management",
      "D. Sales force automation"]
     ),
    ("Which of the following is supported by the marketing business function?",
     ["A. Compensation analysis",
      "B. Process control",
      "C. Credit management",
      "D. Sales force automation"]
     ),
    ("All of the following are supported by the accounting business function except:",
     ["A. General ledger",
      "B. Inventory control",
      "C. Capital budgeting",
      "D. Payroll"]
     ),
    (
        "Providing website visitors with chat rooms, Web forms and questionnaires, and e-mail correspondence opportunities enables companies to use ___ to encourage customers to become involved in product development, delivery, and service issues.",
        ["A. order processing",
         "B. interactive marketing",
         "C. sales force automation",
         "D. None of the choices are correct."]
    ),
    ("Targeted marketing includes all of the following components except:",
     ["A. Online behavior",
      "B. Content",
      "C. Credit",
      "D. Demographics/psychographics"]
     ),
    (
        "Advertising and promotion efforts can be tailored to each visit to a site by an individual. This strategy is based on a variety of tracking techniques, such as Web ___ files recorded on the visitor's disk drive from previous visits.",
        ["A. Virus",
         "B. Donut",
         "C. Cookie",
         "D. Compressed"]
    ),
    (
        "Many companies view sales force automation as a way to gain ___ in sales productivity and marketing responsiveness.",
        ["A. customer loyalty",
         "B. strategic advantage",
         "C. higher profits",
         "D. demographic/psychographic customer statistics"]
    ),
    (
        "___ information systems support the production/operations function that includes all activities concerned with the planning and control of the processes producing goods and services.",
        ["A. Finance",
         "B. Management",
         "C. Marketing",
         "D. Manufacturing"]
    ),
    (
        "Computer integrated manufacturing is an overall concept that stresses using computer-based systems in manufacturing to do all the following, except:",
        ["A. Simplify production processes",
         "B. Automate production processes",
         "C. Integrate all production and support processes",
         "D. Integrate collaboration and communication throughout the organization"]
    ),
    (
        "Computer-integrated manufacturing systems do all the following for activities that are needed to produce products, except:",
        ["A. simplify",
         "B. automate",
         "C. segregate",
         "D. integrate"]
    ),
    (
        "The overall goal of computer-integrated manufacturing is to create flexible, agile, manufacturing processes that do what?",
        ["A. Support the knowledge management processes of the organization.",
         "B. Create products leading specifically to high customer satisfaction.",
         "C. Efficiently produce products of the highest quality.",
         "D. Integrate well into Supply Chain information systems."]
    ),
    ("Computer-integrated manufacturing systems support all of the following concepts except:",
     ["A. Flexible manufacturing systems",
      "B. Inquiry processing",
      "C. Agile manufacturing",
      "D. Total quality management"]
     ),
    (
        "When a manufacturer automates production of a product by installing computer systems to monitor processes and robots to do some of the assembly tasks, it is an example of ___.",
        ["A. computer integrated manufacturing",
         "B. computer-aided manufacturing",
         "C. process control",
         "D. task control"]
    ),
    (
        "When a manufacturer installs performance-monitoring information systems for factory floor operations, it is an example of ___.",
        ["A. computer integrated manufacturing",
         "B. computer-aided manufacturing",
         "C. process control",
         "D. manufacturing execution systems"]
    ),
    (
        "When a manufacturer uses computers to control ongoing physical processes, it is an example of ___.",
        ["A. computer integrated manufacturing",
         "B. computer-aided manufacturing",
         "C. process control",
         "D. manufacturing execution systems"]
    ),
    (
        "Machine control is the use of computers to control the actions of machines. This is also known as ___.",
        ["A. numerical control",
         "B. computer-aided manufacturing",
         "C. process control",
         "D. manufacturing execution systems"]
    ),
    ("Accounting systems are among the ___, yet ___ information systems in business.",
     ["A. newest, least used",
      "B. newest, most widely used",
      "C. oldest, least used",
      "D. oldest, most widely used"]
     ),
    (
        "According to the text, ___ emphasize legal and historical record-keeping and the production of accurate financial statements.",
        ["A. operational accounting systems",
         "B. management accounting systems",
         "C. cross-functional accounting systems",
         "D. financial accounting systems"]
    ),
    (
        "Which of the six essential accounting business systems mentioned in the text reflects changes in inventory and provides shipping and reorder information?",
        ["A. Accounts payable",
         "B. Accounts receivable",
         "C. Inventory control",
         "D. Order processing"]
    ),
    (
        "Which of the six essential accounting business systems mentioned in the text records purchases from, amounts owed to, and payments to suppliers?",
        ["A. Accounts payable",
         "B. Accounts receivable",
         "C. Inventory control",
         "D. Order processing"]
    ),
    (
        "Computer-based ___ systems support business managers and professionals in decisions concerning the financing of a business, and the allocation and control of financial resources within a business.",
        ["A. accounting information",
         "B. financial management",
         "C. marketing information",
         "D. management information"]
    ),
    (
        "Managing the full range of the customer relationship involves two related objectives: (1) providing the organization and all customer-facing employees with a single, complete view of every customer at every touch and across all channels, and (2) providing ___.",
        ["A. suppliers with a single, complete view of the internal workings of the company",
         "B. distributors with a single, complete view of the company and its extended channels",
         "C. customers with a single, complete view of the company and its extended channels",
         "D. customers, suppliers, and investors with a complete view of the internal workings of the company"]
    ),
    (
        "___ systems store customer account data in common databases and then make it available throughout a company via Internet, intranet, or other network links.",
        ["A. Enterprise Resource Planning (ERP)",
         "B. Supply Chain Management (SCM)",
         "C. Customer Relationship Management (CRM)",
         "D. Knowledge Management (KM)"]
    ),
    (
        "CRM systems store customer account data in common databases and then make it available throughout a company via all the following, except: Internet, intranet, or other network links.",
        ["A. Internet",
         "B. Intranet",
         "C. Network links",
         "D. Catalogs"]
    ),
    (
        "CRM software uses information technology to create an enterprisewide system that integrates and automates many of the ___ processes with which customers interact.",
        ["A. sales",
         "B. customer-serving",
         "C. marketing",
         "D. All of the choices are correct."]
    ),
    (
        "Siebel Systems, Oracle, PeopleSoft, SAP AG, and Epiphany are some of the leading vendors of ___ software.",
        ["A. ERP",
         "B. CRM",
         "C. PRM",
         "D. All of the choices are correct."]
    ),
    (
        "A CRM system provides sales reps with the software tools and company data sources they need to ___.",
        ["A. support and manage their sales activities",
         "B. optimize cross-selling",
         "C. optimize up-selling",
         "D. All of the choices are correct."]
    ),
    ("CRM systems help marketing professionals do all of the following except:",
     ["A. Qualify leads for targeted marketing",
      "B. Schedule direct marketing mailings",
      "C. Track direct marketing mailings",
      "D. Build up-to-date marketing brochures"]
     ),
    (
        "CRM systems help fulfill prospect and customer responses and requests by doing all of the following except:",
        ["A. Mailing out additional marketing materials",
         "B. Providing product information",
         "C. Capturing relevant information for the CRM database",
         "D. Quickly scheduling sales contacts"]
    ),
    ("It costs ___ to sell to a new customer than it does to sell to an existing one.",
     ["A. twice as much",
      "B. the same amount",
      "C. six times more",
      "D. half as much"]
     ),
    ("A typical dissatisfied customer will tell ___ about his or her experience.",
     ["A. 8 to 10 people",
      "B. nobody",
      "C. everyone he/she knows",
      "D. 2-4 people"]
     ),
    ("A company can boost its profits ___ by increasing its annual customer retention by only ___.",
     ["A. 8 percent, 10 percent",
      "B. 100 percent, 2 percent",
      "C. 5 percent, 58 percent",
      "D. 85 percent, 5 percent"]
     ),
    (
        "The odds of selling a product to a new customer are ___, whereas the odds of selling a product to an existing customer are ___.",
        ["A. 10 percent, 75 percent",
         "B. 15 percent, 50 percent",
         "C. 5 percent, 20 percent",
         "D. 5 percent, 85 percent"]
    ),
    (
        "If a company takes care of a service problem quickly, ___ of complaining customers will do business with the company again.",
        ["A. 70 percent",
         "B. 15 percent",
         "C. 50 percent",
         "D. 85 percent"]
    ),
    (
        "CRM systems help a company identify, reward, and market to their most loyal and profitable customers through:",
        ["A. Analytical marketing software",
         "B. Databases that include a customer data warehouse and CRM data mart",
         "C. Data mining tools",
         "D. All of the choices are correct."]
    ),
    (
        "A CRM system should support the organization in which phase of the relationship between a business and its customers?",
        ["A. Acquire and enhance",
         "B. Enhance and retain",
         "C. Acquire, enhance, and retain",
         "D. Acquire and retain"]
    ),
    ("A CRM system includes all the following phases, except:",
     ["A. Acquire",
      "B. Enhance",
      "C. Balance",
      "D. Retain"]
     ),
    (
        "The goal of the ___ phase of a customer relationship is to help customers perceive the value of a superior product offered by an outstanding company.",
        ["A. acquire",
         "B. enhance",
         "C. retain",
         "D. all of the choices are correct."]
    ),
    (
        "In the ___ phase of a customer relationship, a business relies on CRM software tools and databases to proactively identify and reward its most loyal and profitable customers via targeted marketing programs.",
        ["A. acquire",
         "B. enhance",
         "C. retain",
         "D. all of the choices are correct."]
    ),
    (
        "In the ___ phase of a customer relationship, CRM account management and customer service and support tools help keep customers happy by supporting superior service from a responsive networked team of sales and service specialists and business partners.",
        ["A. acquire",
         "B. enhance",
         "C. retain",
         "D. all of the choices are correct."]
    ),
    ("Research shows that the major reason for CRM failure is:",
     ["A. senior management opposition",
      "B. lack of support from software vendors",
      "C. lack of understanding and preparation",
      "D. none of the choices are correct."]
     ),
    ("According to the text, common wisdom holds which of the following as a reason for CRM failure?",
     ["A. senior management opposition",
      "B. elongated projects that take on too much, too fast.",
      "C. lack of support from software vendors",
      "D. all of the choices are correct."]
     ),
    (
        "According to the text, common wisdom holds all of the following as reasons for CRM failure, except:",
        ["A. Lack of senior management sponsorship.",
         "B. elongated projects that take on too much, too fast.",
         "C. Lack of end-user incentives leading to poor user adoption rates.",
         "D. All of the choices are correct."]
    ),
    (
        "Increasingly, businesses are moving to ___ CRM systems, to involve business partners as well as customers in collaborative customer services.",
        ["A. operational",
         "B. analytical",
         "C. collaborative",
         "D. portal-based"]
    ),
    ("All of the following are examples of the business value of operational CRM except:",
     ["A. Enables easy collaboration with customers, suppliers, and partners",
      "B. Supports customer interaction with greater convenience through a variety of channels, including phone, fax, e-mail, chat, and mobile devices",
      "C. Synchronizes customer interactions consistently across all channels",
      "D. Makes a company easier to do business with"]
     ),
    ("Which of the following is an example of the business value of collaborative CRM?",
     [
         "A. Provides all users with the tools and information that fit their individual roles and preferences",
         "B. Improves efficiency and integration throughout the supply chain",
         "C. Empowers all employees to respond to customer demands more quickly",
         "D. Synchronizes customer interaction with greater convenience through a variety of channels, including phone, fax, e-mail, chat, and mobile devices"]
     ),
    (
        "A(n) ___ CRM provides all users with the tools and information they need to fit their individual roles and preferences.",
        ["A. operational",
         "B. analytical",
         "C. collaborative",
         "D. portal-based"]
    ),
    (
        "Enterprise resource planning is recognized as a necessary ingredient that many companies need in order to:",
        [
            "A. Gain the efficiency, agility, and responsiveness required to succeed in today's dynamic business environment",
            "B. Maximize their marketing dollars",
            "C. Reduce inventory levels",
            "D. Hold onto competent employees in a competitive environment"]
    ),
    (
        "___ is the technological backbone of e-business, an enterprise-wide transaction framework with links into sales order processing, inventory management and control, production and distribution planning, and finance.",
        ["A. Enterprise resource planning",
         "B. Supply chain management",
         "C. Electronic data interchange",
         "D. Partner relationship management"]
    ),
    (
        "Enterprise resource planning software for a manufacturing company will typically process data from ___.",
        ["A. sales orders and inventory",
         "B. sales, inventory, shipping, and invoicing, as well as from forecasts for raw material and human resources",
         "C. accounts receivable and payable",
         "D. none of the choices are correct."]
    ),
    (
        "According to the textbook case, it took Colgate U.S. anywhere from one to five days to acquire an order and another one to two days to process the order. After ERP, order acquisition and processing combined takes ___.",
        ["A. five days",
         "B. three days",
         "C. 24 hours",
         "D. four hours"]
    ),
    (
        "ERP creates a framework for integrating and improving a company's internal business processes that results in significant improvements in the quality and efficiency of:",
        ["A. Customer service",
         "B. Production",
         "C. Distribution",
         "D. All of the choices are correct."]
    ),
    (
        "ERP systems can provide vital cross-functional information on business performance to managers in a very timely manner. This describes the key business benefit of:",
        ["A. Enterprise agility",
         "B. Decision support",
         "C. Decreased costs",
         "D. Quality and efficiency"]
    ),
    ("Of the typical costs associated with implementing a new ERP system, ___ is the lowest.",
     ["A. hardware",
      "B. software",
      "C. data conversions",
      "D. reengineering"]
     ),
    (
        "Although the benefits of ERP are many, the costs and risks can be considerable. Which of the following make up the bulk of the cost of implementing a new ERP system?",
        ["A. Hardware",
         "B. Software",
         "C. Reengineering (developing new business processes)",
         "D. Converting data from legacy systems"]
    ),
    ("Which of the following has been a major cause of failure in ERP projects?",
     [
         "A. Business managers and IT professionals underestimating the complexity of the planning, development, and training needed",
         "B. Trying to do too much too fast",
         "C. Insufficient training in the new work tasks required by the ERP system",
         "D. All of the choices are correct."]
     ),
    (
        "According to the textbook case, Visa's ___ management infrastructure was fragmented, complex, and costly to maintain.",
        ["A. human resources",
         "B. financial",
         "C. marketing",
         "D. communications"]
    ),
    (
        "Fundamentally, ___ helps a company get the right products to the right place at the right time, in the proper quantity, and at an acceptable cost.",
        ["A. customer relationship management",
         "B. supply chain management",
         "C. electronic data interchange",
         "D. partner relationship management"]
    ),
    (
        "The goal of SCM is to create a fast, efficient, and low-cost network of business relationships, or a ___, to get a company's products from concept to market.",
        ["A. supply chain",
         "B. service chain",
         "C. product chain",
         "D. relationship chain"]
    ),
    (
        "Because each supply chain process should add value to the products or services a company produces, a supply chain is frequently called a ___ chain.",
        ["A. process",
         "B. service",
         "C. product",
         "D. value"]
    ),
    (
        "A typical box of breakfast cereal takes ___ to get from factory to supermarket, struggling its way through wholesalers, distributors, brokers, and consolidators, each of which has a warehouse.",
        ["A. seven days",
         "B. 30 days",
         "C. over 100 days",
         "D. six months"]
    ),
    (
        "The demands of today's competitive business environment are pushing manufacturers to use which of the following technologies to help them re-engineer their relationships with suppliers, distributors, and retailers?",
        ["A. Intranets",
         "B. Extranets",
         "C. E-commerce Web portals",
         "D. All of the choices are correct."]
    ),
    ("Which of the following correctly describes the supply chain life cycle supported by SCM systems?",
     ["A. Commit, schedule, make, and deliver",
      "B. Buy, make, sell",
      "C. Buy, sell, schedule, deliver",
      "D. None of the choices are correct."]
     ),
    (
        "___ involves the electronic exchange of business transaction documents over the Internet and other networks between supply chain trading partners (organizations and their customers and suppliers).",
        ["A. Data exchange",
         "B. Intranets",
         "C. Electronic data interchange",
         "D. Data interchange"]
    ),
    (
        "EDI is still a popular data-transmission format among major trading partners, primarily to automate repetitive transactions, though it is slowly being replaced by ___-based Web services.",
        ["A. HTML",
         "B. Intranet",
         "C. Web-2",
         "D. XML"]
    ),
    (
        "According to the textbook case, Telefonica realized that many smaller businesses could not afford standard EDI services, so they offered InfoEDI which allows transmission to be entered and processed ___.",
        ["A. on data exchanges",
         "B. on intranets",
         "C. on the Internet",
         "D. on extranets"]
    ),
    ("All of the following are strategic SCM objectives and outcomes except:",
     ["A. Establishing policies",
      "B. Designing a network",
      "C. Establishing objectives",
      "D. Scheduling production"]
     ),
    ("Which of the following is a tactical SCM objective?",
     ["A. Deploying resources to match supply to demand",
      "B. Monitoring, controlling, and adjusting production",
      "C. Changing transportation methods",
      "D. Establishing objectives and policies"]
     ),
    ("All of the following are operation SCM objectives and outcomes except:",
     ["A. Schedule and monitor production",
      "B. Control and adjust production",
      "C. Order/inventory tracking",
      "D. Material movement"]
     ),
    ("Which of the following is a execution SCM objective?",
     ["A. Build and transport",
      "B. Monitoring, controlling, and adjusting production",
      "C. Changing transportation methods",
      "D. Establishing objectives and policies"]
     ),
    (
        "Optimize network of suppliers, plants, and distribution centers is an outcome of the ___ SCM function.",
        ["A. supply chain design",
         "B. materials management",
         "C. collaborative fulfillment",
         "D. supply chain event management"]
    ),
    (
        "Develop an accurate forecast of customer demand by sharing demand and supply forecasts instantaneously across multiple tiers is an outcome of the ___ SCM function.",
        ["A. supply chain design",
         "B. collaborative demand and supply planning",
         "C. collaborative fulfillment",
         "D. supply chain event management"]
    ),
    ("Sharing of accurate inventory and procurement information is an outcome of the ___ SCM function.",
     ["A. supply chain design",
      "B. materials management",
      "C. collaborative fulfillment",
      "D. supply chain event management"]
     ),
    (
        "Optimize plans and schedules while considering resource, material, and dependency constraints is an outcome of the ___ SCM function.",
        ["A. supply chain design",
         "B. materials management",
         "C. collaborative fulfillment",
         "D. collaborative manufacturing"]
    ),
    (
        "Support the entire logistics process, including picking, packing, shipping, and delivery in foreign countries is an outcome of the ___ SCM function.",
        ["A. supply chain design",
         "B. materials management",
         "C. collaborative fulfillment",
         "D. supply chain event management"]
    ),
    (
        "Monitor every stage of the supply chain process, from price quotation to the moment the customer receives the product is an outcome of the ___ SCM function.",
        ["A. supply chain design",
         "B. materials management",
         "C. collaborative fulfillment",
         "D. supply chain event management"]
    ),
    (
        "Report key measurements in the supply chain, such as filling rates, order cycle times, and capacity utilization is an outcome of the ___ SCM function.",
        ["A. supply chain performance management",
         "B. materials management",
         "C. collaborative fulfillment",
         "D. supply chain event management"]
    ),
    ("SCM systems generally provide companies with all of the following benefits except:",
     ["A. Lower marketing costs",
      "B. Quicker times to market",
      "C. Reductions in inventory levels",
      "D. Lower transaction and materials costs"]
     ),
    (
        "Companies employing supply chain management systems can still face problems. Which of the following is not identified as a cause of SCM problems in the text?",
        ["A. A lack of demand planning knowledge",
         "B. Inaccurate production or inventory data provided by a company's other information systems",
         "C. Inaccurate or overly-optimistic demand forecasts",
         "D. Too many solutions from which to choose"]
    ),
    (
        "A lack of adequate collaboration between suppliers, distributors, and ___ departments within a company will sabotage any SCM system.",
        ["A. marketing",
         "B. production",
         "C. inventory management",
         "D. All of the choices are correct."]
    ),
    ("Nike's failed SCM implementation resulted in all the following except:",
     ["A. $100 million in lost sales",
      "B. 50% of the Nike factories were closed",
      "C. Depressed stock prices",
      "D. Class action lawsuits"]
     ),
    (
        "Companies in stage ___ of a supply chain management implementation concentrate on making improvements to internal supply chain processes and external processes and relationships with suppliers and customers.",
        ["A. one",
         "B. two",
         "C. three",
         "D. four"]
    ),
    (
        "Companies in stage ___ of a supply chain management implementation concentrate on expanding the business network of Web-enabled SCM-capable trading partners in their supply chain to increase operational efficiency and effectiveness in meeting strategic business objectives.",
        ["A. one",
         "B. two",
         "C. three",
         "D. four"]
    ),
    (
        "Companies in stage ___ of a supply chain management implementation strive to optimize the development and management of their supply chains in order to meet strategic customer value and business value goals.",
        ["A. one",
         "B. two",
         "C. three",
         "D. four"]
    ),
    ("Which of the following would occur in stage 3 of a supply chain management implementation?",
     ["A. Order fulfillment",
      "B. Collaborative marketing",
      "C. Order management",
      "D. Resource allocation"]
     ),
    ("Which of the following would occur in stage 1 of a supply chain management implementation?",
     ["A. Logistics",
      "B. Collaborative marketing",
      "C. Order management",
      "D. Resource allocation"]
     ),
    ("According to the textbook case, SCM software:",
     ["A. allows McKesson to monitor CVS's store level consumption and inventory",
      "B. allows CVS to monitor McKesson's store level consumption and inventory",
      "C. allows McKesson to see what items CVS is ordering from other vendors",
      "D. allows CVS to place orders with vendors other than McKesson"]
     ),
    ("According to the text, which of the following choices correctly describes e-commerce?",
     ["A. Buying and selling products online",
      "B. Reliance on Internet-based technologies and e-commerce to accomplish marketing, discovery, transaction processing, and product and consumer service processes",
      "C. Business-to-consumer online marketing, selling, and transaction processing",
      "D. Business-to-business, business-to-consumer, and consumer-to-consumer online transactions"]
     ),
    ("E-commerce includes all of the following except:",
     ["A. E-business processes, such as extranet access of inventory databases",
      "B. Intranet access of customer relationship management systems by sales and customer service reps",
      "C. Customer collaboration in product development via e-mail exchanges",
      "D. Acceptance of payments through ATM networks"]
     ),
    (
        "In a typical e-commerce process, ___ notify suppliers of a new Request For Quote (RFQ) via e-mail.",
        ["A. back-office application servers",
         "B. storage-area networks",
         "C. database servers",
         "D. Web servers"]
    ),
    ("Which of the following is not one of the three basic categories of electronic commerce?",
     ["A. Government-to-business",
      "B. Business-to-consumer",
      "C. Business-to-business",
      "D. Consumer-to-consumer"]
     ),
    (
        "Electronic personal advertising of products or services to consumers at ___ is an important form of C2C e-commerce.",
        ["A. electronic newspaper sites",
         "B. consumer e-commerce portals",
         "C. personal websites",
         "D. All of the choices are correct."]
    ),
    (
        "Authenticating users, authorizing access, and enforcing security features is a component of the e-commerce process called:",
        ["A. Event notification",
         "B. Profiling and personalization",
         "C. Search management",
         "D. Access control and security"]
    ),
    (
        "The e-commerce component that deals with gathering data on customers and their website behavior and choices is:",
        ["A. Event notification",
         "B. Profiling and personalizing",
         "C. Search management",
         "D. Access control and security"]
    ),
    (
        "When a company addresses issues such as authenticating users of their website, authorizing access, and enforcing the security features that protect both consumers and their data, the company is addressing the ___ component of the e-commerce process.",
        ["A. event notification",
         "B. profiling and personalizing",
         "C. search management",
         "D. access control and security"]
    ),
    (
        "The e-commerce component that deals with developing efficient and effective processes to help customers find the specific product or service they want to evaluate or buy is:",
        ["A. Event notification",
         "B. Profiling and personalizing",
         "C. Search management",
         "D. Content management"]
    ),
    (
        "When accessing an e-commerce site, you will generally be given access to all of the following except:",
        ["A. Webmaster administration areas",
         "B. Product databases",
         "C. Online ordering systems",
         "D. Online customer support"]
    ),
    (
        "___ software works with workflow management software to monitor all e-commerce processes and record all relevant events, including unexpected changes or problem situations.",
        ["A. Supply Chain Management (SCM)",
         "B. Customer Relationship Management (CRM)",
         "C. Enterprise Resource Planning (ERP)",
         "D. Event notification"]
    ),
    (
        "___ helps employees electronically collaborate to accomplish structured work tasks within knowledge-based business processes, using predefined sets of business rules, roles of stakeholders, authorization requirements, routing alternatives, databases, and the sequence of tasks required for each e-commerce process.",
        ["A. Groupware",
         "B. Knowledge management software",
         "C. Database software",
         "D. Workflow management software"]
    ),
    (
        "Most e-commerce systems on the Web involving business and consumers (B2C) depend on ___ payment processes.",
        ["A. cash-on-delivery",
         "B. purchase order",
         "C. electronic check",
         "D. credit card"]
    ),
    (
        "Event notification software works with workflow management software to do all the following, except:",
        ["A. Monitor all e-commerce processes",
         "B. Record all relevant events",
         "C. Record unexpected changes or problem situations",
         "D. Provide catalog and content information to prospective customers."]
    ),
    (
        "Payment processes for e-commerce transaction are ___ due to ___ nature of the transactions taking place between the networked computer systems of buyers and sellers.",
        ["A. Complex; the near-anonymous electronic",
         "B. Simple; the very specific manual",
         "C. Complex; the very specific manual",
         "D. Simple; the near-anonymous electronic"]
    ),
    (
        "When customers can select products from website catalog displays and put them into a virtual holding bin for later checkout and processing, they are using a ___.",
        ["A. shopping cart",
         "B. configuration queue",
         "C. PayPal register",
         "D. shopping queue"]
    ),
    ("Banking networks support teller terminals at ___ and automated teller machines (ATMs) at ___.",
     ["A. all bank offices; locations throughout the world",
      "B. any bank; local bank branches",
      "C. all bank offices; local bank branches",
      "D. any bank; locations throughout the world"]
     ),
    ("Electronic funds transfer systems:",
     ["A. Handle most forms of electronic payment in the banking and retailing industries",
      "B. Use a variety of information technologies to capture and process money and credit transfers between banks, business, and customers",
      "C. Make it possible for consumers to use a credit or debit card to instantly pay for purchases at retail outlets",
      "D. All of the choices are correct."]
     ),
    (
        "The text describes a number of measures that are being developed in order to solve security problems associated with online credit card purchases. Which of the following statements is not one of those measures?",
        ["A. Encryption of data passing between the customer and the merchant",
         "B. Encryption of data passing between the customer and the company authorizing the credit card transaction",
         "C. Delaying shipment of items purchased until the purchaser is authenticated",
         "D. Taking sensitive data offline"]
    ),
    (
        "Many companies use the SSL security method developed by Netscape Communication that automatically encrypts data passing between a Web browser and a merchant's server. SSL stands for:",
        ["A. Secure Socket Level",
         "B. Secure Socket Layer",
         "C. Security Safety Latching",
         "D. Safe Server Listing"]
    ),
    (
        "Firms such as VISA, MasterCard, IBM, Microsoft, and Netscape have agreed to SET which stands for:",
        ["A. Satellite Encrypted Transfer",
         "B. Strongly Encrypted Telecommunications",
         "C. Secure Electronic Transaction",
         "D. Smooth eFunds Transaction"]
    ),
    ("E-commerce is changing how companies do business both internally and externally with their ___.",
     ["A. customers",
      "B. business partners",
      "C. suppliers",
      "D. All of the choices are correct."]
     ),
    ("E-commerce applications that focus on the consumer share all of the following goals except:",
     ["A. Attracting potential buyers",
      "B. Handling goods and services transactions",
      "C. Building customer loyalty",
      "D. Duplicating successful website layouts and functions"]
     ),
    ("Which of the following would generally take the longest time to implement?",
     ["A. Interactive marketing",
      "B. Procurement automation",
      "C. Web storefront and e-catalog",
      "D. Self-service Web sales"]
     ),
    ("Which of the following is considered a B2B project?",
     ["A. Interactive marketing",
      "B. Self-service Web sales",
      "C. Integrated Web store",
      "D. Extranets and exchanges"]
     ),
    (
        "A basic fact for Internet retailing is that all retail websites are created equal as far as the ___ imperative of success in retailing is concerned.",
        ["A. advertising",
         "B. integration",
         "C. location",
         "D. pricing"]
    ),
    ("All the following factors are key to e-tailing, except:.",
     ["A. Selection and value",
      "B. Security and reliability",
      "C. Locating the business close to the customers",
      "D. Look and feel of the Website"]
     ),
    ("Which statement best addresses the e-commerce success factor of selection and value?",
     [
         "A. I don't want to browse through a slow website or buy from a site where paying takes too long.",
         "B. Your prices don't have to be the lowest on the Web as long as you have a reputation for high quality, guaranteed satisfaction, and customer support.",
         "C. I want to know about sales when I log onto a site and get free shipping if the value of my order exceeds a certain amount.",
         "D. I want to receive the exact product that I ordered, within the timeframe promised."]
     ),
    ("Which of the following is an example of a traditional market communication?",
     ["A. Niche magazine ads",
      "B. Buttons",
      "C. Banners",
      "D. Sponsorships"]
     ),
    (
        "The statement Most business-to-consumer sites offer consumers incentives to buy and return, such as coupons, discounts, special offers, and vouchers for other Web services reflects the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Selection and value",
         "C. Advertising and incentives",
         "D. Look and feel"]
    ),
    (
        "Easy-to-find contact information, online order status, and product support specialists are part of the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Selection and value",
         "C. Advertising and incentives",
         "D. Great customer communication"]
    ),
    (
        "Trustworthy product information and reliable order fulfillment are part of the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Security and reliability",
         "C. Advertising and incentives",
         "D. Great customer communication"]
    ),
    (
        "Attractive Web storefront, Web site shopping areas, multimedia product catalog pages, and shopping features are part of the ___ success factor for retailing on the Web.",
        ["A. Look and feel",
         "B. Selection and value",
         "C. Advertising and incentives",
         "D. Great customer communication"]
    ),
    (
        "Competitive prices, satisfaction guarantees, and customer support after the sale are part of the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Selection and value",
         "C. Advertising and incentives",
         "D. Great customer communication"]
    ),
    (
        "Fast and easy navigation, shopping, and purchasing, and prompt shipping and delivery are part of the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Selection and value",
         "C. Advertising and incentives",
         "D. Great customer communication"]
    ),
    (
        "Web advertising, e-mail notices, and interactive support for all customers are part of the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Selection and value",
         "C. Personal attention",
         "D. Great customer communication"]
    ),
    (
        "Linking of customers, suppliers, company representatives, and others via newsgroups, chat rooms, and links to related sites are part of the ___ success factor for retailing on the Web.",
        ["A. Performance and service efficiency",
         "B. Selection and value",
         "C. Personal attention",
         "D. Community relationships"]
    ),
    (
        "The statement Give online customers with similar interests a feeling of belonging to a unique group of like-minded individuals reflects the ___ success factor for retailing on the Web.",
        ["A. performance and service efficiency",
         "B. community relationships",
         "C. personalization",
         "D. look and feel"]
    ),
    (
        "Which of the following statements reflects the e-commerce success factor of security and reliability?",
        ["A. I want to be able to quickly find what I'm looking for.",
         "B. I want the lowest price on the Web, every time.",
         "C. I'm looking for a huge variety of goods and services.",
         "D. I want to receive my order in the timeframe promised."]
    ),
    ("The Amazon Giver application does which of the following?",
     ["A. Allows MySpace members the ability to buy gifts for each other.",
      "B. Allows FaceBook members the ability to buy gifts for each other.",
      "C. Allows MySpace members the ability to sell items to each other.",
      "D. Allows FaceBook members the ability to sell items to each other."]
     ),
    ("The Amazon Grapevine application does which of the following?",
     ["A. Provides MySpace members with news feeds from the latest news sources.",
      "B. Provides FaceBook members with news feeds from the latest news sources.",
      "C. Provides MySpace members with news feeds of friends' activities on Amazon.",
      "D. Provides FaceBook members with news feeds of friends' activities on Amazon."]
     ),
    (
        "Building an e-commerce website can be done in a number of ways. Which of the following would a small company with limited capital most likely choose as a cost-effective option?",
        ["A. Use the website design tools and predesigned templates provided by a website host",
         "B. Use in-house personnel or outside website developers to build a custom-designed site",
         "C. Share the cost of developing a website by partnering with companies that offer similar products and services",
         "D. Buy an existing website"]
    ),
    ("All of the following are examples of customer support except:",
     ["A. Online help",
      "B. Links to related sites",
      "C. Shipping and tax calculations",
      "D. Discussion groups and chat rooms"]
     ),
    (
        "All of the following are examples of the web store requirements that must be implemented in order to serve customers as they select an item and pay for it except:",
        ["A. E-mail order notifications",
         "B. Shipping and tax calculations",
         "C. Credit card processing",
         "D. Gift wrapping and gift card options"]
    ),
    (
        "According to the text, most business-to-consumer e-commerce ventures take the form of ___ on the World Wide Web.",
        ["A. Auction sites",
         "B. Retail business sites",
         "C. Bricks-and-mortar sites",
         "D. None of the above"]
    ),
    ("Online user profiles are commonly developed through all of the following methods except:",
     ["A. User registration",
      "B. Cookie files",
      "C. User feedback",
      "D. Telephone surveys"]
     ),
    (
        "Wholesale (B2B) electronic commerce relies on different information technologies, most of which can be implemented on all the following, except:",
        ["A. The Internet",
         "B. The World Wide Web",
         "C. Corporate intranets or extranets",
         "D. Stand-alone legacy systems"]
    ),
    (
        "The latest e-commerce transaction systems are scaled and customized to allow buyers and sellers to meet in a variety of high-speed trading platforms, such as:",
        ["A. Auctions",
         "B. Catalogs",
         "C. Exchanges",
         "D. All of the choices are correct."]
    ),
    (
        "A ___ buy-side marketplace attracts many suppliers that flock to the exchange to bid for the business of a major buyer, such as GE or AT&T.",
        ["A. many-to-one",
         "B. some-to-many",
         "C. many-to-some",
         "D. many-to-many"]
    ),
    (
        "A ___ procurement marketplace unites major buyers who combine their purchasing catalogs to attract more suppliers, and thus more competition and lower prices.",
        ["A. many-to-one",
         "B. some-to-many",
         "C. many-to-some",
         "D. many-to-many"]
    ),
    (
        "A ___ auction marketplace can be used by many buyers and sellers, who can create a variety of auctions to dynamically optimize prices.",
        ["A. many-to-one",
         "B. some-to-many",
         "C. many-to-some",
         "D. many-to-many"]
    ),
    (
        "A ___ sell-side marketplace hosts one major supplier who dictates product catalog offerings and prices.",
        ["A. many-to-one",
         "B. one-to-many",
         "C. many-to-some",
         "D. many-to-many"]
    ),
    (
        "A ___ distribution marketplace unites major suppliers who combine their product catalogs to attract a larger audience of buyers.",
        ["A. many-to-one",
         "B. some-to-many",
         "C. many-to-some",
         "D. many-to-many"]
    ),
    ("E-commerce portals provide all of the following types of marketplaces except:",
     ["A. Catalog",
      "B. Community",
      "C. Exchange",
      "D. Auction"]
     ),
    (
        "In a B2B e-commerce Web portal configuration, a ___ collects and tracks bids from buyers and sellers.",
        ["A. B2B web portal",
         "B. market generator server",
         "C. content manager server",
         "D. post-trade market history server"]
    ),
    (
        "In a B2B e-commerce Web portal configuration, aggregated product data is retrieved from a ___ and loaded into a live market server.",
        ["A. B2B web portal",
         "B. market generator server",
         "C. content manager server",
         "D. post-trade market history server"]
    ),
    (
        "Which of the following statements about how using a B2B e-commerce site impacts the purchasing decisions of a business is false?",
        ["A. Purchasing is more cost effective",
         "B. Purchasing is faster",
         "C. Purchasing is more simple",
         "D. Purchasing transactions are easier to trace"]
    ),
    ("The organization that controls spectrum is the ___.",
     ["A. FAA",
      "B. FFA",
      "C. CDC",
      "D. FCC"]
     ),
    (
        "When companies have both e-commerce virtual business operations and traditional physical business operations, they must decide whether to integrate the two or keep them separate. Office Depot was cited in the text as a company that:",
        ["A. Kept the .com sales channel separate from the traditional business operations",
         "B. Fully integrated the .com sales channel into their traditional business operations",
         "C. Partially integrated the .com sales channel into their traditional business operations",
         "D. Dropped its .com sales channel due to a lack of profitability"]
    ),
    (
        "After considering a broad spectrum of alternatives and benefits trade-offs, Barnes and Noble decided to:",
        ["A. Spin-off its e-commerce business",
         "B. Engage in a joint venture with another book vendor",
         "C. Move its e-commerce business to an in-house division",
         "D. Integrate its physical and e-commerce businesses"]
    ),
    ("Integration of a physical and e-commerce business results in all of the following except:",
     ["A. Brand establishment",
      "B. Greater focus",
      "C. Shared information",
      "D. Purchasing leverage"]
     ),
    (
        "Which of the following companies entered into a joint venture in order to handle the e-commerce side of its business?",
        ["A. Barnes and Noble",
         "B. Rite Aid",
         "C. KB Toys",
         "D. Office Depot"]
    ),
    ("All of the following are key questions for developing an e-commerce channel strategy except:",
     ["A. How many employees do we want to assign to the project?",
      "B. What audiences are we trying to reach?",
      "C. Who owns the e-commerce channel within the organization?",
      "D. How well will our brands translate to the new channel?"]
     ),
    (
        "The type of information required by decision makers in a company is directly related to the level of management decision making and the amount of ___ in the decision situations they face.",
        ["A. financial risk",
         "B. structure",
         "C. variable information",
         "D. urgency"]
    ),
    ("Which of the following statements most accurately describes the operational level of management?",
     [
         "A. Composed of a board of directors and an executive committee of the CEO and top executives who develop overall organizational goals, strategies, policies, and objectives as part of a strategic planning process",
         "B. Composed of self-directed teams and middle managers, who develop short-and medium-range plans, schedules, and budgets",
         "C. Composed of self-directed teams or supervisory managers who develop short-range plans, according to procedures and within the budgets and schedules established for the teams and other workgroups of the organization",
         "D. None of the choices are correct."]
     ),
    ("Decisions made at the tactical management level tend to be more:",
     ["A. Structured",
      "B. Semi-structured",
      "C. Unstructured",
      "D. Self-structured"]
     ),
    ("Decisions made at the strategic management level tend to be more:",
     ["A. Structured",
      "B. Semi-structured",
      "C. Unstructured",
      "D. All the choices are correct."]
     ),
    (
        "Deciding what product lines to develop over the next five years is an example of a(n) ___ decision.",
        ["A. structured",
         "B. semi-structured",
         "C. unstructured",
         "D. open-ended"]
    ),
    ("Which of the following statements is a characteristic of the content dimension of information?",
     ["A. Information is provided when it is needed.",
      "B. Information is related to the information needs of a specific recipient for a specific situation.",
      "C. Information is provided in an easy-to-understand form.",
      "D. Information is presented in a narrative, numeric, or graphic form."]
     ),
    ("Which of the following statements is a characteristic of the form dimension of information?",
     ["A. Information is based on past, present, or future time periods.",
      "B. Information is arranged in a predetermined sequence.",
      "C. All the information needed is provided.",
      "D. The information can have a broad or narrow scope, or an internal or external focus."]
     ),
    ("___ is an example of an unstructured, operational management decision.",
     ["A. Cash management",
      "B. Program control",
      "C. Product planning",
      "D. Capital budgeting"]
     ),
    ("___ is an example of a structured, tactical management decision.",
     ["A. Program control",
      "B. Employee performance appraisal",
      "C. Credit management",
      "D. Company reorganization"]
     ),
    ("Business intelligence applications are based on all of the following except:",
     ["A. Personalized and Web-enabled information analysis",
      "B. Knowledge management",
      "C. Rapid information input processes",
      "D. Decision support technologies"]
     ),
    ("Decision support systems use ___ to support the making of semi-structured business decisions.",
     ["A. analytical models",
      "B. specialized databases",
      "C. a decision maker's own insights and judgments",
      "D. All of the choices are correct."]
     ),
    (
        "Dell, Wal-Mart, and Amazon are a few of the companies using ___ DSS models to stimulate and optimize supply chain flow and reduce inventory levels.",
        ["A. pricing",
         "B. product and service quality",
         "C. financial performance",
         "D. supply chain"]
    ),
    (
        "Harrah's, Capital One, and Barclays are a few of the companies using ___ DSS models to identify customers who produce the greatest profit.",
        ["A. loyalty and service",
         "B. product and service quality",
         "C. customer selection",
         "D. financial performance"]
    ),
    ("The information products from an MIS take all the following forms except:",
     ["A. scheduled reports.",
      "B. exception reports.",
      "C. push reports.",
      "D. pull reports."]
     ),
    ("A weekly sales report is a typical example of a(n) ___ report.",
     ["A. periodic scheduled",
      "B. exception",
      "C. demand",
      "D. action"]
     ),
    (
        "A major freight company has several thousand drivers. A report containing information about only those company drivers who have not taken a mandatory defensive driving course is an example of a(n) ___ report.",
        ["A. periodic scheduled",
         "B. exception",
         "C. demand",
         "D. action"]
    ),
    ("With ___, information is available whenever a manager demands it.",
     ["A. push reporting",
      "B. exception reports",
      "C. periodic scheduled reports",
      "D. demand reports and responses"]
     ),
    ("Online analytical processes involve all of the following analytical operations except:",
     ["A. Consolidation",
      "B. Filtration",
      "C. Drill-down",
      "D. Slicing and dicing"]
     ),
    (
        "With ___, data about sales offices can be rolled up to the district level, and district-level data can be rolled up to provide a regional-level perspective.",
        ["A. consolidation",
         "B. drill-down",
         "C. filtration",
         "D. slicing and dicing"]
    ),
    (
        "Many companies are using GIS technology along with global positioning system devices to do all of the following except:",
        ["A. Map customer traffic patterns within each store",
         "B. Choose new retail store locations",
         "C. Optimize distribution routes",
         "D. Analyze the demographics of their target audiences"]
    ),
    (
        "Using a decision support system involves all of the following types of analytical modeling activities except ___ analysis.",
        ["A. sensitivity",
         "B. exception",
         "C. what-if",
         "D. goal-seeking"]
    ),
    (
        "Which one of the following should be used to answer the question, What would happen to sales if we cut advertising by 25 percent?",
        ["A. Goal-seeking",
         "B. Optimization",
         "C. Sensitivity",
         "D. What-if"]
    ),
    (
        "What type of analysis should be used to respond to the statement, Let's cut advertising by $1000 repeatedly so we can see its relationship to sales?",
        ["A. Goal-seeking",
         "B. Optimization",
         "C. Sensitivity",
         "D. What-if"]
    ),
    (
        "___ analysis involves making repeated changes to selected variables until a chosen variable reaches a target value.",
        ["A. What-if",
         "B. Sensitivity",
         "C. Goal-seeking",
         "D. Optimization"]
    ),
    (
        "___ analysis is a more complex form of goal-seeking where the goal is to find the best value for a target variable given certain constraints.",
        ["A. What-if",
         "B. Sensitivity",
         "C. Market basket",
         "D. Optimization"]
    ),
    ("Which of the following is one of the most common and useful types of data mining for marketing?",
     ["A. Goal seeking analysis",
      "B. Market basket analysis",
      "C. Optimization analysis",
      "D. Sensitivity analysis"]
     ),
    (
        "The purpose of ___ is to determine what products customers purchase together with other products.",
        ["A. a regression decision tree",
         "B. neural networks",
         "C. cluster detection",
         "D. market basket analysis"]
    ),
    (
        "By targeting customers who are already known to be likely buyers, the effectiveness of a given marketing effort is significantly increased—if the marketing takes the form of ___.",
        ["A. in-store displays",
         "B. catalogs",
         "C. a direct offer",
         "D. The form of the marketing does not matter."]
    ),
    (
        "According to the textbook case, Warner Home Video is using ___ to forecast the number of video disks going to retail stores.",
        ["A. online order entry statistics",
         "B. mail order catalog data",
         "C. business intelligence applications",
         "D. none of the choices are correct."]
    ),
    ("Decision support in business is changing, driven by all of the following except:",
     ["A. Changing corporate spending patterns",
      "B. Rapid developments in end user computing and networking",
      "C. Internet and Web technologies",
      "D. Web-enabled business applications"]
     ),
    (
        "A(n) ___ is a Web-based interface and integration of MIS, DSS, EIS, and other technologies that gives all intranet users and selected extranet users access to a variety of internal and external business applications and services.",
        ["A. enterprise Resource System",
         "B. enterprise Information Portal",
         "C. executive Information System",
         "D. collaborative Information System"]
    ),
    (
        "Internal enterprise information portal applications typically include access to all of the following except:",
        ["A. E-mail and project websites",
         "B. Human resources Web self-services",
         "C. Internet news services",
         "D. Corporate databases"]
    ),
    ("According to the text, an enterprise knowledge portal has all of the following except:",
     ["A. Personalized views of news and data",
      "B. Desktop publishing tools",
      "C. Collaboration tools",
      "D. Community work areas"]
     ),
    ("Which of the following is an example of an unstructured data source?",
     ["A. ERP database",
      "B. CRM database",
      "C. Other databases",
      "D. E-mail"]
     ),
    ("Artificial intelligence is a science and technology based on:",
     ["A. Computer science",
      "B. Biology and psychology",
      "C. Linguistics and mathematics",
      "D. All of the choices are correct."]
     ),
    (
        "Who was the British AI pioneer responsible for proposing a test for determining if machines could think?",
        ["A. Alan Turing",
         "B. John McCarthy",
         "C. Allen Nevell",
         "D. Herbert Simon"]
    ),
    ("AI applications can be grouped under all of the following areas except:",
     ["A. Cognitive science",
      "B. Robotics",
      "C. Natural interfaces",
      "D. Linguistics"]
     ),
    (
        "All of the following are attributes of intelligent behavior that AI attempts to duplicate except:",
        ["A. Reasoning and learning",
         "B. Emotion",
         "C. Problem solving",
         "D. Responding quickly and successfully to new situations"]
    ),
    (
        "All of the following would be considered an AI application in the cognitive science group except:",
        ["A. Expert systems",
         "B. Neural networks",
         "C. Speech recognition",
         "D. Learning systems"]
    ),
    ("All of the following would be considered an AI application in the robotics group except:",
     ["A. Visual perception",
      "B. Neural networks",
      "C. Locomotion",
      "D. Navigation"]
     ),
    (
        "All of the following would be considered an AI application in the natural interface group except:",
        ["A. Visual perception",
         "B. Speech recognition",
         "C. Multisensory interfaces",
         "D. Virtual reality"]
    ),
    (
        "Which of the following represents knowledge in the form of past performance, occurrences, and experiences?",
        ["A. Case-based reasoning",
         "B. Frame-based knowledge",
         "C. Object-based knowledge",
         "D. Rule-based knowledge"]
    ),
    (
        "Which of the following represents knowledge in the form of a hierarchy or network of collections consisting of a complex package of data values describing its attributes?",
        ["A. Case-based reasoning",
         "B. Frame-based knowledge",
         "C. Object-based knowledge",
         "D. Rule-based knowledge"]
    ),
    (
        "Which of the following represents knowledge in the form of a network of data elements including both the data and the methods/processes that act on those data?",
        ["A. Case-based reasoning",
         "B. Frame-based knowledge",
         "C. Object-based knowledge",
         "D. Rule-based knowledge"]
    ),
    (
        "Which of the following represents knowledge in the form of statements of fact, typically in the form of premise and conclusion?",
        ["A. Case-based reasoning",
         "B. Frame-based knowledge",
         "C. Object-based knowledge",
         "D. Rule-based knowledge"]
    ),
    (
        "Which of the following artificial intelligence applications can learn by processing sample problems and their solutions?",
        ["A. Knowledge-based systems",
         "B. Neutral networks",
         "C. Expert systems",
         "D. Fuzzy logic systems"]
    ),
    ("Which of the following is an example of a robotics application of AI?",
     [
         "A. Intelligent work environment that helps capture the why and the what of engineered design and decision making",
         "B. Machine-vision inspection systems for gauging, guiding, identifying, and inspecting products and providing competitive advantage in manufacturing",
         "C. Automated animation interfaces that allow users to interact with virtual objects via touch",
         "D. Situation assessment and resource allocation software for uses that range from airlines and airports to logistics centers"]
     ),
    (
        "Within an expert system, the ___ contains facts about a specific subject area and rules that express the reasoning procedures of an expert on the subject.",
        ["A. inference engine",
         "B. knowledge engineer",
         "C. knowledge base",
         "D. None of the choices are correct."]
    ),
    ("According to the text, all of the following are considered benefits of an expert system except:",
     ["A. It is cheaper to employ than multiple human experts",
      "B. It can outperform a single human expert in many situations",
      "C. An expert system is faster and more consistent than human experts",
      "D. It does not get tired or distracted"]
     ),
    ("According to the text, all of the following are major limitations of an expert system except:",
     ["A. It has a limited focus",
      "B. Users of the system have a high learning curve",
      "C. It is unable to learn",
      "D. It is costly to develop"]
     ),
    (
        "An equipment calibration expert system is an example of an expert system in the application category of:",
        ["A. Decision management",
         "B. Selection/classification",
         "C. Process monitoring/control",
         "D. Diagnostic/troubleshooting"]
    ),
    (
        "An inventory control expert system is an example of an expert system in the application category of:",
        ["A. Decision management",
         "B. Selection/classification",
         "C. Process monitoring/control",
         "D. Diagnostic/troubleshooting"]
    ),
    (
        "An employee performance evaluation expert system is an example of an expert system in the application category of:",
        ["A. Decision management",
         "B. Selection/classification",
         "C. Process monitoring/control",
         "D. Diagnostic/troubleshooting"]
    ),
    (
        "A suspect identification expert system is an example of an expert system in the application category of:",
        ["A. Decision management",
         "B. Diagnostic/troubleshooting",
         "C. Design/configuration",
         "D. Selection/classification"]
    ),
    (
        "A communications network expert system is an example of an expert system in the application category of:",
        ["A. Decision management",
         "B. Design/configuration",
         "C. Process monitoring/control",
         "D. Diagnostic/troubleshooting"]
    ),
    (
        "All of the following would be controlled by the process monitoring/control category of expert systems except:",
        ["A. Chemical testing",
         "B. Material selection",
         "C. Inventory control",
         "D. Production monitoring"]
    ),
    ("All of the following are suitability criteria for expert systems except:",
     ["A. Viability",
      "B. Domain",
      "C. Expertise",
      "D. Structure"]
     ),
    ("Which of the following would be considered a fuzzy logic term?",
     ["A. Above ten",
      "B. Very low",
      "C. Over ten",
      "D. Between one and five"]
     ),
    (
        "Genetic algorithms were first used to simulate millions of years in ___ evolution in just a few minutes on a computer.",
        ["A. biological",
         "B. geological",
         "C. ecosystem",
         "D. All of the choices are correct."]
    ),
    (
        "Multisensory input/output devices, such as data gloves or jumpsuits, are commonly used with ___ systems.",
        ["A. knowledge-based",
         "B. neural network",
         "C. virtual reality",
         "D. fuzzy logic"]
    ),
    (
        "___ is commonly used by pharmaceutical and biotechnology firms to develop and observe the behavior of computerized models of new drugs and materials.",
        ["A. Fuzzy logic",
         "B. Virtual reality",
         "C. A neural network",
         "D. An expert system"]
    ),
    ("An intelligent agent is:",
     ["A. A software surrogate that accomplishes specific tasks for users",
      "B. Database software used to analyze current sales trends",
      "C. A marketing software system used to do statistical analysis",
      "D. A software package used by robots"]
     ),
    ("The use of intelligent agents is growing rapidly as a way to do all of the following except:",
     ["A. Simplify software use",
      "B. Search websites on the Internet and on corporate intranets",
      "C. Make matches on Internet dating sites",
      "D. Facilitate comparison shopping among the many e-commerce sites on the Web"]
     ),
    (
        "___ planning involves the setting of objectives and the development of procedures, rules, schedules, and budgets.",
        ["A. Strategic",
         "B. Operational",
         "C. Tactical",
         "D. All of the choices are correct."]
    ),
    ("___ planning is done on a short-term basis to implement and control day-to-day operations.",
     ["A. Strategic",
      "B. Operational",
      "C. Tactical",
      "D. Scenario"]
     ),
    (
        "All of the following are examples of questions that would be asked when establishing an understanding the customer strategic vision except:",
        ["A. Who are our customers?",
         "B. How can we add value for the customer with e-business services?",
         "C. How are our customers' priorities shifting?",
         "D. Who should be our target customers?"]
    ),
    (
        "Which of the following is an example of questions that would be asked when establishing a customer value strategic vision?",
        ["A. Who are our customers?",
         "B. How can we add value for the customer with e-business services?",
         "C. How are our customers' priorities shifting?",
         "D. Who should be our target customers?"]
    ),
    (
        "All of the following are examples of questions that would be asked when establishing a competition strategic vision except:",
        ["A. Who are our real competitors?",
         "B. How are our competitor's priorities shifting?",
         "C. What is our toughest competitor's business model?",
         "D. Are our competitors potential partners, supplies, or customers in an e-business venture?"]
    ),
    (
        "Which of the following is a question that would be asked when establishing a value chain strategic vision?",
        ["A. Who are our customers?",
         "B. How can we add value for the customer with e-business services?",
         "C. Are our competitors potential partners, supplies, or customers in an e-business venture?",
         "D. Who would be our supply chain partners?"]
    ),
    (
        "A demand for better and more convenient solutions is a ___ trend that is shaping strategic business/IT planning.",
        ["A. technology",
         "B. competitive imperatives",
         "C. deregulation",
         "D. customer sophistication/expectations"]
    ),
    (
        "A situation where previously regulated markets are opening is a ___ trend that is shaping strategic business/IT planning.",
        ["A. technology",
         "B. competitive imperatives",
         "C. deregulation",
         "D. customer sophistication/expectations"]
    ),
    (
        "Outsourcing, growth, and customer orientation are ___ trends that are shaping strategic business/IT planning.",
        ["A. technology",
         "B. competitive imperatives",
         "C. deregulation",
         "D. customer sophistication/expectations"]
    ),
    (
        "Technology convergence, increasing information content, and e-commerce are ___ trends that are shaping strategic business/IT planning.",
        ["A. technology",
         "B. competitive imperatives",
         "C. deregulation",
         "D. customer sophistication/expectations"]
    ),
    ("All of the following are considered competitive forces except:",
     ["A. Cost leadership",
      "B. Competitors",
      "C. Customers",
      "D. New entrants"]
     ),
    ("All of the following are considered competitive strategies except:",
     ["A. Differentiation",
      "B. Innovation",
      "C. New entrants",
      "D. Alliances"]
     ),
    (
        "___ are areas of substandard business performance compared to others in the industry or market segments.",
        ["A. Weaknesses",
         "B. Opportunities",
         "C. Threats",
         "D. Strengths"]
    ),
    (
        "___ are the potential for new business markets or innovative breakthroughs that might expand present markets.",
        ["A. Weaknesses",
         "B. Opportunities",
         "C. Threats",
         "D. Strengths"]
    ),
    (
        "___ are the potential for business and market losses posed by competitors, competitive forces, government, or disruptive technologies.",
        ["A. Weaknesses",
         "B. Opportunities",
         "C. Threats",
         "D. Strengths"]
    ),
    ("___ are core competencies and resources where a firm is a market or industry leader.",
     ["A. Weaknesses",
      "B. Opportunities",
      "C. Threats",
      "D. Strengths"]
     ),
    (
        "Offering customers something distinctive or at a lower cost than competitors is a component of the ___ business model.",
        ["A. revenue source",
         "B. pricing",
         "C. sustainability",
         "D. customer value"]
    ),
    (
        "Which of the following questions best represents the sustainability component of a business model?",
        ["A. What is it about the firm that makes it difficult for other firms to imitate it?",
         "B. What are the firm's capabilities and capabilities gaps that need to be filled?",
         "C. Where do the dollars come from?",
         "D. To which customers is the firm offering this value?"]
    ),
    (
        "The question How many new activities must be performed as a result of the Internet? best represents the ___ component of e-business models.",
        ["A. scope",
         "B. connected activities",
         "C. implementation",
         "D. sustainability"]
    ),
    ("According to the text case, which of the following is not an IT risk?",
     ["A. Program Risk",
      "B. Market Risk",
      "C. Business Operations Risk",
      "D. Technology Risk"]
     ),
    (
        "The ___ component of the business/IT planning process involves making strategic IT choices that reflect an information technology architecture designed to support a company's e-business and other business/IT initiatives.",
        ["A. resource management",
         "B. technology architecture",
         "C. strategic development",
         "D. All of the choices are correct."]
    ),
    (
        "The ___ component of the business/IT planning process involves developing strategic plans for managing or outsourcing a company's IT resources.",
        ["A. resource management",
         "B. technology architecture",
         "C. strategic development",
         "D. All of the choices are correct."]
    ),
    (
        "The ___ component of the business/IT planning process involves developing business strategies that support a company's business vision, using IT to create innovative e-business systems focusing on customer and business value.",
        ["A. resource management",
         "B. technology architecture",
         "C. strategic development",
         "D. All of the choices are correct."]
    ),
    (
        "The ___ component of the information technology architecture includes the networks, computer systems, system software, and integrated enterprise application software that provide the computing and communications platform supporting the strategic use of information technology.",
        ["A. IT organization",
         "B. data resources",
         "C. technology platform",
         "D. applications architecture"]
    ),
    (
        "The ___ component of the information technology architecture includes the many operational and specialized databases that store and provide data and information for business process and decision support.",
        ["A. IT organization",
         "B. data resources",
         "C. technology platform",
         "D. applications architecture"]
    ),
    (
        "The ___ component of the information technology architecture includes business applications designed as an integrated architecture of enterprise systems that support strategic business initiatives.",
        ["A. IT organization",
         "B. data resources",
         "C. technology platform",
         "D. applications architecture"]
    ),
    (
        "The ___ component of the information technology architecture includes the organizational structure of the IS function within a company and the distribution of IS specialists, designed to meet the changing strategies of a business.",
        ["A. IT organization",
         "B. data resources",
         "C. technology platform",
         "D. applications architecture"]
    ),
    (
        "Having a ___ perspective means measuring financial performance, such as number of debtors, cash flow, or return on investment.",
        ["A. learning and growth",
         "B. customer",
         "C. financial",
         "D. business process"]
    ),
    ("Having a ___ perspective means reflecting on the performance of key business processes.",
     ["A. learning and growth",
      "B. customer",
      "C. financial",
      "D. business process"]
     ),
    (
        "Having a ___ perspective means measuring the company's learning curve, such as the time spent on staff training.",
        ["A. learning and growth",
         "B. customer",
         "C. financial",
         "D. business process"]
    ),
    (
        "A company that measures the time it takes to process a phone call, tabulates the results of customer surveys, and tracks the number of user complains has a ___ perspective.",
        ["A. learning and growth",
         "B. customer",
         "C. financial",
         "D. business process"]
    ),
    (
        "The most valuable Internet applications allow companies to transcend communication barriers and establish connections that will do all of the following except:",
        ["A. Enhance productivity",
         "B. Stimulate innovative development",
         "C. Improve customer relations",
         "D. Increase the quality of job applicants"]
    ),
    (
        "E-mail, chat systems, discussion groups, and a company website are typical examples of the ___ quadrant of a strategic positioning matrix.",
        ["A. global market penetration",
         "B. product and service transformation",
         "C. cost and efficiency improvements",
         "D. performance improvement in business effectiveness"]
    ),
    (
        "A company that enters the ___ quadrant of a strategic positioning matrix must capitalize on a high degree of customer and competitor connectivity and use of IT.",
        ["A. global market penetration",
         "B. product and service transformation",
         "C. cost and efficiency improvements",
         "D. performance improvement in business effectiveness"]
    ),
    (
        "A company that enters the ___ quadrant of a strategic positioning matrix has a high degree of internal connectivity and pressures to improve its business processes.",
        ["A. global market penetration",
         "B. product and service transformation",
         "C. cost and efficiency improvements",
         "D. performance improvement in business effectiveness"]
    ),
    (
        "A company that enters the ___ quadrant of a strategic positioning matrix is extensively networked with its customers, suppliers, and competition through Web sites, intranets, and extranets.",
        ["A. global market penetration",
         "B. product and service transformation",
         "C. cost and efficiency improvements",
         "D. performance improvement in business effectiveness"]
    ),
    (
        "The ___ model supplements, rather than replaces, physical distribution and marketing channels. Examples are Cisco and Dell.",
        ["A. market creator",
         "B. channel reconfiguration",
         "C. channel mastery",
         "D. All of the choices are correct."]
    ),
    (
        "The ___ model requires you to be among the first to market and to remain ahead of competition by continuously innovating. Examples are Amazon.com and E*TRADE.",
        ["A. self-service innovator",
         "B. supply chain innovator",
         "C. channel mastery",
         "D. market creator"]
    ),
    (
        "The ___ model supplants, rather than replaces, existing physical business offices and call centers by using the Internet as a sales and service channel.",
        ["A. self-service innovator",
         "B. supply chain innovator",
         "C. channel mastery",
         "D. market creator"]
    ),
    (
        "The ___ model uses the Internet to streamline the interactions among all parties in the supply chain to improve operating efficiency.",
        ["A. self-service innovator",
         "B. supply chain innovator",
         "C. channel mastery",
         "D. market creator"]
    ),
    (
        "The ___ model uses the Internet to provide a comprehensive suite of services that the customer's employees can use directly.",
        ["A. self-service innovator",
         "B. supply chain innovator",
         "C. channel mastery",
         "D. market creator"]
    ),
    (
        "The ___ model uses the Internet to reduce search costs and offers the customer a unified process for collecting information necessary to make a large purchase.",
        ["A. infomediary",
         "B. supply chain innovator",
         "C. channel mastery",
         "D. market creator"]
    ),
    (
        "The ___ model uses the Internet to process purchases, including the process of searching, comparing, selecting, and paying online.",
        ["A. infomediary",
         "B. supply chain innovator",
         "C. channel mastery",
         "D. transaction intermediary"]
    ),
    (
        "A business application planning process includes consideration of IT proposals for all of the following except:",
        ["A. Addressing strategic business priorities",
         "B. Building business cases",
         "C. Planning for application development",
         "D. Planning for application implementation"]
    ),
    (
        "New business processes are stored in a ___ of reusable business models and application components.",
        ["A. repository",
         "B. bank",
         "C. database",
         "D. All of the choices are correct."]
    ),
    ("Implementing new business/IT strategies requires managing the effects of major changes in ___.",
     ["A. business processes",
      "B. managerial roles",
      "C. employee work assignments",
      "D. All of the choices are correct."]
     ),
    (
        "Which of the following is not considered one of the top ten enterprise resource planning challenges?",
        ["A. Organizing the data",
         "B. Getting end user buy-in",
         "C. Dealing with multiple/international sites and partners",
         "D. Moving to a new platform"]
    ),
    ("Which of the following is the biggest obstacle to knowledge management systems?",
     ["A. Cost",
      "B. Immature technology",
      "C. User resistance to sharing knowledge",
      "D. Immaturity of knowledge management industry"]
     ),
    ("According to the text case, the original Iridium organization failed because:",
     ["A. the company couldn't afford to keep the system updated.",
      "B. Iridium focused on the wrong business.",
      "C. the system was not operational before the company went through a merger.",
      "D. satellite phones do not work indoors."]
     ),
    (
        "According to the textbook case, all of the following were causes for the failure of the Iridium project except:",
        ["A. the service was too expensive.",
         "B. the phone only worked outdoors.",
         "C. the original phone was too bulky.",
         "D. the phones were never properly tested."]
    ),
    ("Which of the following is part of the technology dimension of change management?",
     ["A. Ownership",
      "B. Recruitment",
      "C. Enterprise architecture",
      "D. Change control"]
     ),
    (
        "Implementing a new e-business application, such as customer relationship management might involve:",
        ["A. Developing a change action plan",
         "B. Assigning selected managers as change sponsors",
         "C. Developing employee change teams",
         "D. All of the choices are correct."]
    ),
    (
        "Change experts recommend all of the following tactics to reduce the risks and cost and to maximize the benefits of change except:",
        ["A. Change the company culture before the project is implemented, not after",
         "B. Involve as many people as possible in e-business planning and application development",
         "C. Keep constant change an expected part of the culture",
         "D. Make liberal use of financial incentives and recognition"]
    ),
    (
        "All of the following are examples of the actions that would normally be taken while defining a change strategy except:",
        ["A. Assess readiness for change",
         "B. Select the best change configuration",
         "C. Establish change governance",
         "D. Promote leadership resolve"]
    ),
    (
        "Which of the following is an action that would normally be taken while trying to build commitment to an impending change?",
        ["A. Develop leadership capability",
         "B. Transfer knowledge and skills",
         "C. Create a compelling change story",
         "D. Implement culture change"]
    ),
    (
        "All of the following are actions that would be taken while attempting to develop a culture of change except:",
        ["A. Understand the current culture",
         "B. Design the target organization",
         "C. Implement cultural change",
         "D. Merging new employees (fresh blood) into the existing culture."]
    ),
    (
        "All of the following are actions that would be taken while attempting to develop a change in vision except:",
        ["A. Understand the strategic vision",
         "B. Assess the organization's readiness for change",
         "C. Create a compelling change story",
         "D. Make the vision operational and comprehensive"]
    ),
    (
        "According to the text case, senior managers finally realized that IT personnel ___ functional or divisional heads who are largely concerned with their own areas.",
        ["A. often have a similar view of the organization to",
         "B. often have a more comprehensive view of the organization than many",
         "C. often have a less comprehensive view of the organization than many",
         "D. none of the above"]
    ),
    (
        "According to the textbook case, what was the final stage of organizational transformation for Reuters as it sought to implement global shared service centers for its financial services function?",
        ["A. Organizational redesign",
         "B. Technology enablement",
         "C. Sourcing redesign",
         "D. Business process redesign"]
    ),
    ("Which of the following is the initial stage of an organizational transformation?",
     ["A. Organizational redesign",
      "B. Technology enablement",
      "C. Sourcing redesign",
      "D. Business process redesign"]
     ),
    ("Systems thinking means that an individual sees:",
     ["A. Inter-relationships among systems and processes",
      "B. Discrete snapshots of change, whenever it occurs",
      "C. Linear cause-and-effects when events occur",
      "D. All of the choices are correct."]
     ),
    ("Systems thinking means all the following, except:",
     ["A. Seeing inter-relationships among systems and processes",
      "B. Seeing processes of change among systems, rather than discrete snapshots of change",
      "C. Seeing linear cause-and-effects when events occur",
      "D. Seeing the forest and the trees in any situation"]
     ),
    (
        "The overall process by which information systems are designed and implemented within organizations is referred to as systems ___.",
        ["A. design",
         "B. analysis",
         "C. analysis and design",
         "D. implementation"]
    ),
    ("Which of the following correctly reflects the stages of the system development life cycle?",
     ["A. Investigation, analysis, implementation, and maintenance",
      "B. Analysis, design, and implementation",
      "C. Investigation, analysis, design, implementation, and maintenance",
      "D. Investigation, prototyping, design, conversion, and change management"]
     ),
    (
        "A feasibility study is a preliminary study to investigate the information needs of prospective users and is used to determine the proposed system's ___.",
        ["A. resource requirements",
         "B. costs and benefits",
         "C. feasibility",
         "D. All of the choices are correct."]
    ),
    (
        "All of the following are done during the systems implementation stage of application development, except:",
        ["A. Develop logical models of the current system",
         "B. Acquire or develop hardware and software",
         "C. Convert to the new business system",
         "D. Manage the effects of system changes on end users"]
    ),
    (
        "All of the following are done during the systems investigation stage of application development, except:",
        ["A. Develop logical models of the current system",
         "B. Conduct a feasibility study",
         "C. Determine how to address business opportunities and priorities",
         "D. Develop a project management plan and obtain management approval"]
    ),
    ("Which of the following is done during the systems analysis stage of application development?",
     ["A. Develop logical models of the current system",
      "B. Conduct a feasibility study",
      "C. Develop logical models of new system",
      "D. Test the system, and train people to operate and use it"]
     ),
    ("Which of the following is done during the systems design stage of application development?",
     ["A. Develop logical models of the current system",
      "B. Conduct a feasibility study",
      "C. Develop logical models of new system",
      "D. Convert to the new business system"]
     ),
    ("Which of the following is done during the systems maintenance stage of application development?",
     ["A. Develop logical models of the current system",
      "B. Monitor, evaluate, and modify the business system as needed",
      "C. Develop logical models of new system",
      "D. Convert to the new business system"]
     ),
    ("A feasibility study will answer all of the following questions except:",
     ["A. Does the technology exist that is necessary to implement the proposed system?",
      "B. Is the proposed system technologically, economically, and operationally feasible?",
      "C. Which brand and model of computer will be used by the proposed system?",
      "D. What impact will the proposed system have on current employees?"]
     ),
    (
        "The ___ feasibility assessment focuses on the degree to which the proposed development project fits with the existing business environment and objectives, with regard to development schedule, delivery date, corporate culture, and existing business processes.",
        ["A. technical",
         "B. legal/political",
         "C. economic",
         "D. operational"]
    ),
    (
        "According to the text, certain changes in ___ may dictate the need for change, regardless of the assessed feasibility of such change.",
        ["A. the business environment",
         "B. product specifications",
         "C. management structure",
         "D. technical system requirements"]
    ),
    (
        "Determining whether expected cost savings, increased profits, and other benefits exceed the cost of developing and operating a system is related to ___ feasibility.",
        ["A. economic",
         "B. functional",
         "C. operational",
         "D. system"]
    ),
    (
        "Dealing with patents, copyrights, and licensing for a proposed system is related to ___ feasibility.",
        ["A. economic",
         "B. technical",
         "C. operational",
         "D. legal/political"]
    ),
    ("Economic feasibility is concerned with:",
     [
         "A. How well a proposed information system supports the objectives of the organization and its strategic plan for information systems",
         "B. Whether expected cost savings, increased revenue, increased profits, reductions in required investment, and other types of benefits will exceed the cost of developing and operating a proposed system",
         "C. Determining if reliable hardware and software capable of meeting the needs of a proposed system can be acquired or developed by the business in the required time",
         "D. The willingness and ability of management, employees, customers, suppliers, and others to operate, use, and support a proposed system"]
     ),
    ("Which of the following factors is related to technical feasibility?",
     ["A. Customer acceptance",
      "B. Governmental restrictions",
      "C. Cost savings",
      "D. Network reliability"]
     ),
    ("Which of the following is related to human factors feasibility?",
     ["A. Customer acceptance",
      "B. How well the proposed system will fit with the existing organizational structure",
      "C. Increased profits",
      "D. Hardware capability"]
     ),
    ("Which of the following is an example of an intangible cost?",
     ["A. Employee salaries",
      "B. Loss of customer goodwill",
      "C. Reduced inventory-carrying costs",
      "D. Improved customer service"]
     ),
    (
        "Which category of feasibility study focuses on determining if reliable hardware and software, capable of meeting the needs of a proposed system, can be acquired or developed in the required time?",
        ["A. Economic",
         "B. Operational",
         "C. Technical",
         "D. Legal/political"]
    ),
    ("All of the following would be a focus of a human factors feasibility study except:",
     ["A. Acceptance by employees",
      "B. How well a proposed system fits the company plans",
      "C. Customer and supplier acceptance",
      "D. All of the choices are factors in human factors feasibility."]
     ),
    ("All of the following would be a focus of a legal/political feasibility study except:",
     ["A. Copyright or patent infringements",
      "B. Links to grassroots political parties",
      "C. Identifying the key stakeholders and the degree to which the proposed system may affect the distribution of power",
      "D. Existing contractual obligations"]
     ),
    ("Which of the following is a function of the systems analysis stage?",
     ["A. Conducting a feasibility study",
      "B. Developing the functional requirements of the system",
      "C. Writing program code",
      "D. Data conversion"]
     ),
    ("Why are business end users frequently added to system development teams?",
     ["A. They have the greatest stake in a successful product",
      "B. They know a lot about the business activities that affect the company's business processes",
      "C. They are usually experienced in IS development",
      "D. They are the most likely to eliminate unnecessary documentation and steps"]
     ),
    ("A logical model of a current system is a blueprint of:",
     ["A. How the current system does what it does",
      "B. What the current system does, without regard to how it does it",
      "C. What the system does and how it does it",
      "D. Documentation of what the new system will look like and how it will work"]
     ),
    (
        "Fast retrieval and update of data from product, pricing, and customer databases is an example of a ___ requirement.",
        ["A. user interface",
         "B. processing",
         "C. control",
         "D. storage"]
    ),
    (
        "Automatic entry of product data and easy-to-use data entry screens for Web customers are examples of a ___ requirement.",
        ["A. user interface",
         "B. processing",
         "C. control",
         "D. storage"]
    ),
    (
        "Fast, automatic calculation of sales totals and shipping costs is an example of a ___ requirement.",
        ["A. user interface",
         "B. processing",
         "C. control",
         "D. storage"]
    ),
    (
        "Signals for data entry errors and quick e-mail confirmation for customers are examples of a ___ requirement.",
        ["A. user interface",
         "B. processing",
         "C. control",
         "D. storage"]
    ),
    (
        "During the physical design stage, users and analysts focus on determining ___ the system will accomplish its objectives.",
        ["A. how",
         "B. when",
         "C. where",
         "D. All of the choices are correct."]
    ),
    ("Prototyping involves:",
     ["A. A standard systems development cycle using CASE tools",
      "B. The rapid generation of a system by IS professionals, without the need for end user input",
      "C. An interative, interactive development process with extensive end user involvement",
      "D. A fail-safe development process designed to ensure that an information system meets all user requirements, without revision"]
     ),
    ("Which of the following statements most accurately applies to the concept of prototyping?",
     ["A. Prototyping is not practical for large-scale projects",
      "B. Prototyping produces an actual working model of the information system needed by users",
      "C. Prototyping emphasizes getting the design right the first time",
      "D. Prototyping reduces the need for user involvement in systems development"]
     ),
    ("Which of the following statements applies to end user development?",
     [
         "A. IS professionals play a consulting role, while end users do their own application development",
         "B. Focus should be on the fundamental activities of any information system: input, processing, output, storage, and control",
         "C. Users develop new or improved ways to perform your jobs without the direct involvement of IS specialists",
         "D. All of the choices are correct."]
     ),
    ("User interface design refers to the development of:",
     ["A. Programs and procedures to be used by end-users",
      "B. Display screens, forms and reports, and interactive computer user dialogs",
      "C. User training manuals",
      "D. The structure of databases and files accessible by end users"]
     ),
    (
        "In analyzing a potential application, you should focus first on the ___ to be produced by the application.",
        ["A. input",
         "B. processing",
         "C. storage",
         "D. output"]
    ),
    ("When analyzing a potential application, the proper order of actions should be:",
     ["A. input, output, processing",
      "B. processing, output, input",
      "C. input, processing, output",
      "D. output, input, processing"]
     ),
    ("Control measures for end user applications vary greatly depending upon the:",
     ["A. Number and nature of the users of the application",
      "B. Scope and duration of the application",
      "C. Nature of the data involved",
      "D. All of the choices are correct."]
     ),
    ("The systems implementation stage of application development involves:",
     ["A. Hardware and software acquisition",
      "B. Conversion of data resources",
      "C. Testing of programs and procedures",
      "D. All of the choices are correct."]
     ),
    ("Which of the following is recognized as an idea to spur end user Web development?",
     ["A. Spur creativity",
      "B. Make users comfortable",
      "C. Set limits",
      "D. All of the choices are correct."]
     ),
    ("No matter what the project, all of the following elements are necessary except:",
     ["A. Prototypes",
      "B. Process",
      "C. Tools",
      "D. Techniques"]
     ),
    (
        "All of the following are activities performed during the initiating/defining project management phase except:",
        ["A. Stating the problems/goals",
         "B. Securing resources",
         "C. Writing a detailed project plan",
         "D. Exploring costs/benefits with a feasibility study"]
    ),
    (
        "Which of the following are activities performed during the initiating/defining project management phase?",
        ["A. Establish reporting obligations",
         "B. Securing resources",
         "C. Commit resources to specific tasks",
         "D. Meet with stakeholders"]
    ),
    (
        "All of the following are activities performed during the planning project management phase except:",
        ["A. Stating the problems/goals",
         "B. Identify the critical path",
         "C. Writing a detailed project plan",
         "D. Estimate time and resources needed for completion"]
    ),
    ("Which of the following are activities performed during the planning project management phase?",
     ["A. Establish reporting obligations",
      "B. Identify and sequence activities",
      "C. Commit resources to specific tasks",
      "D. Meet with stakeholders"]
     ),
    (
        "All of the following are activities performed during the executing project management phase except:",
        ["A. Commit resources to specific tasks",
         "B. Add additional resources/personnel if necessary",
         "C. Writing a detailed project plan",
         "D. Initiate project work"]
    ),
    ("Which of the following are activities performed during the executing project management phase?",
     ["A. Establish reporting obligations",
      "B. Identify and sequence activities",
      "C. Commit resources to specific tasks",
      "D. Meet with stakeholders"]
     ),
    (
        "All of the following are activities performed during the controlling project management phase except:",
        ["A. Create reporting tools",
         "B. Compare actual progress with baseline",
         "C. Establish reporting obligations",
         "D. Writing a detailed project plan"]
    ),
    ("Which of the following are activities performed during the controlling project management phase?",
     ["A. Establish reporting obligations",
      "B. Identify and sequence activities",
      "C. Commit resources to specific tasks",
      "D. Meet with stakeholders"]
     ),
    (
        "All of the following are activities performed during the closing project management phase except:",
        ["A. Install all deliverables",
         "B. Release project resources",
         "C. Document the project",
         "D. Writing a detailed project plan"]
    ),
    ("Which of the following are activities performed during the closing project management phase?",
     ["A. Meet with stakeholders",
      "B. Identify and sequence activities",
      "C. Commit resources to specific tasks",
      "D. Establish reporting obligations"]
     ),
    (
        "Which of the following activities would normally be performed during the closing project management phase?",
        ["A. Document the project",
         "B. Establish reporting obligations",
         "C. Compare actual progress with baseline",
         "D. Initiate control interventions, if necessary"]
    ),
    (
        "According to the text, what is probably the most important contribution of the modern project management approach?",
        ["A. Identifying the project as a series of steps",
         "B. Recognizing the importance of user input to the project",
         "C. Eliminating the input of information system specialists",
         "D. None of the selections are considered the most important"]
    ),
    (
        "The most important objective to achieve during the ___ phase is the clear and succinct statement of the problem that the project is to solve, or the goals that it is to achieve.",
        ["A. initiating/defining",
         "B. planning",
         "C. executing",
         "D. controlling"]
    ),
    ("The acronym RFP stands for:",
     ["A. Request for pricing",
      "B. Request for proposal",
      "C. Request for flat pricing",
      "D. Request for fixed pricing"]
     ),
    ("When a company needs to evaluate competing proposals for hardware or software acquisition:",
     ["A. Each evaluation factor is assigned an equal weight",
      "B. Each evaluation factor is assigned a different number of points, depending on its importance to the company",
      "C. The lowest bid is always the ultimate selection factor",
      "D. Only three things matter: cost, performance, and support"]
     ),
    (
        "The question of compatibility with hardware and software being provided by competing suppliers is a ___ evaluation factor.",
        ["A. performance",
         "B. compatibility",
         "C. technology",
         "D. connectivity"]
    ),
    ("Software packages that are ___ aren't a good choice at any price.",
     ["A. slow",
      "B. hard to use",
      "C. poorly documented",
      "D. All of the choices are correct."]
     ),
    ("Which of the following statements about documentation is true?",
     [
         "A. Documentation is no longer important because commercial software has online help systems, backed up with Internet-based help systems",
         "B. Documentation serves as a method of communication among the people who develop, implement, and maintain a system",
         "C. Only program modifications and/or customizations need to be documented",
         "D. Documentation is the most expensive part of any system implementation"]
     ),
    (
        "A large retail company with many locations may choose to use a conversion strategy in which the new system is put in place at only one location. This method of conversion is called ___ conversion.",
        ["A. parallel",
         "B. pilot",
         "C. phased",
         "D. direct"]
    ),
    ("According to the text, adaptive maintenance includes:",
     ["A. Fixing software bugs and logic errors not detected during the implementation testing period",
      "B. Modifying existing functions or adding new functionality to accommodate changes in the business or operating environments",
      "C. Reducing the chances of system failure or extending the capacity of a current system's useful life",
      "D. Making changes to an existing system that are intended to improve the performance of a function or interface"]
     ),
    ("According to the text, corrective maintenance includes:",
     ["A. Fixing software bugs and logic errors not detected during the implementation testing period",
      "B. Modifying existing functions or adding new functionality to accommodate changes in the business or operating environments",
      "C. Reducing the chances of system failure or extending the capacity of a current system's useful life",
      "D. Making changes to an existing system that are intended to improve the performance of a function or interface"]
     ),
    ("According to the text, preventative maintenance includes:",
     ["A. Fixing software bugs and logic errors not detected during the implementation testing period",
      "B. Modifying existing functions or adding new functionality to accommodate changes in the business or operating environments",
      "C. Reducing the chances of system failure or extending the capacity of a current system's useful life",
      "D. Making changes to an existing system that are intended to improve the performance of a function or interface"]
     ),
    ("According to the text, perfective maintenance includes:",
     ["A. Fixing software bugs and logic errors not detected during the implementation testing period",
      "B. Modifying existing functions or adding new functionality to accommodate changes in the business or operating environments",
      "C. Reducing the chances of system failure or extending the capacity of a current system's useful life",
      "D. Making changes to an existing system that are intended to improve the performance of a function or interface"]
     ),
    (
        "Evaluating and acquiring necessary hardware and software resources and information system services is a(n) ___ activity.",
        ["A. acquisition",
         "B. software development",
         "C. documentation",
         "D. conversion"]
    ),
    (
        "Developing software that will not be acquired externally and making necessary modifications to software packages that are acquired is a(n) ___ activity.",
        ["A. acquisition",
         "B. software development",
         "C. documentation",
         "D. conversion"]
    ),
    (
        "Changing data in company databases to new data formats and subsets required by newly installed software is a(n) ___ activity.",
        ["A. acquisition",
         "B. software development",
         "C. documentation",
         "D. conversion"]
    ),
    (
        "Educating management, end users, customers, and other business stakeholders to develop user competencies is a(n) ___ activity.",
        ["A. acquisition",
         "B. testing",
         "C. documentation",
         "D. training"]
    ),
    (
        "Assessing and making necessary corrections to the programs, procedures, and hardware used by a new system is a(n) ___ activity.",
        ["A. acquisition",
         "B. software development",
         "C. testing",
         "D. conversion"]
    ),
    (
        "Recording and communicating detailed system specifications, including procedures for end users and IS personnel and examples of input screens, output displays, and reports, is a(n) ___ activity.",
        ["A. acquisition",
         "B. software development",
         "C. documentation",
         "D. conversion"]
    ),
    (
        "Switching from the use of a present system to the operation of a new or improved system is a(n) ___ activity.",
        ["A. acquisition",
         "B. software development",
         "C. documentation",
         "D. conversion"]
    ),
    (
        "As a business professional, you have a responsibility to promote ethical uses of information technology in the workplace. This responsibility includes:",
        [
            "A. Performing your role as a vital business resource by participating on every development team",
            "B. Using the Internet only during breaks and after-work hours",
            "C. Performing your role as a vital human resource in the business systems you help develop and use in your organization",
            "D. Documenting all employee electronic mail usage and Internet searches"]
    ),
    (
        "According to the text, information technology has caused ethical controversy in all of the following basic categories of ethical business issues, except:",
        ["A. Intellectual property rights",
         "B. Whistle blowing",
         "C. Customer and employee privacy",
         "D. Workplace safety"]
    ),
    (
        "According to the text, information technology has caused ethical controversy in which of the following basic categories of ethical business issues?",
        ["A. Comparable worth",
         "B. Whistle blowing",
         "C. Workplace safety",
         "D. Employee conflicts of interest"]
    ),
    (
        "According to the text, which are the four basic categories of ethical business issues where information technology has caused ethical controversy?",
        [
            "A. Intellectual property rights, customer and employee privacy, security of company information, and workplace safety",
            "B. Executive salaries, affirmative action, whistle blowing, and advertising content",
            "C. Product pricing, shareholder interests, inappropriate gifts, divestment",
            "D. Comparable worth, sexual harassment, employee conflicts of interest, product safety"]
    ),
    (
        "When managers apply the ___ theory of ethical decision making, they believe that companies have ethical responsibilities to all members of society.",
        ["A. social contract",
         "B. stakeholder",
         "C. stockholder",
         "D. Midas"]
    ),
    (
        "When managers apply the ___ theory of ethical decision making, they believe that managers have an ethical responsibility to manage a firm for the benefit of all individuals and groups that have a claim on a company.",
        ["A. social contract",
         "B. stakeholder",
         "C. stockholder",
         "D. Midas"]
    ),
    (
        "When managers apply the ___ theory of ethical decision making, they believe their only responsibility is to increase the profits of the business without violating the law or engaging in fraudulent practices.",
        ["A. social contract",
         "B. stakeholder",
         "C. stockholder",
         "D. Midas"]
    ),
    ("The social contract theory maintains that:",
     [
         "A. Companies have ethical responsibilities to all members of society, which allow corporations to exist based on a social contract",
         "B. Managers are agents of the organization's owners, and their only ethical responsibility is to increase the profits of the business without violating the law or engaging in fraudulent practices",
         "C. Managers have an ethical responsibility to manage a firm for the benefit of all individuals and groups that have a claim on a company",
         "D. Managers are agents of the customer, and their only ethical responsibility is to increase the service of the business, without violating the law or engaging in fraudulent practices"]
     ),
    ("The stockholder theory maintains that:",
     [
         "A. Companies have ethical responsibilities to all members of society, which allow corporations to exist based on a social contract",
         "B. Managers are agents of the organization's owners, and their only ethical responsibility is to increase the profits of the business without violating the law or engaging in fraudulent practices",
         "C. Managers have an ethical responsibility to manage a firm for the benefit of all individuals and groups that have a claim on a company",
         "D. Managers are agents of the customer, and their only ethical responsibility is to increase the service of the business, without violating the law or engaging in fraudulent practices"]
     ),
    ("The stakeholder theory maintains that:",
     [
         "A. Companies have ethical responsibilities to all members of society, which allow corporations to exist based on a social contract",
         "B. Managers are agents of the organization's owners, and their only ethical responsibility is to increase the profits of the business without violating the law or engaging in fraudulent practices",
         "C. Managers have an ethical responsibility to manage a firm for the benefit of all individuals and groups that have a claim on a company",
         "D. Managers are agents of the customer, and their only ethical responsibility is to increase the service of the business, without violating the law or engaging in fraudulent practices"]
     ),
    (
        "According to the text, all the following are examples of ethical behavior by organizations, except:",
        ["A. Scheduling work breaks",
         "B. Stockholder theory",
         "C. Limiting exposure to computer monitors",
         "D. Preventing hand or eye injuries"]
    ),
    (
        "One of the major principles of technology ethics is that the good achieved by the technology must outweigh the harm or risk. Moreover, there must be no alternative that achieves the same or comparable benefits with less harm or risk. This principle is:",
        ["A. Informed consent",
         "B. Justice",
         "C. Minimized risk",
         "D. Proportionality"]
    ),
    ("Which of the following best describes the ethical principle of informed consent?",
     [
         "A. The good achieved by technology must outweigh the harm or risk. Moreover, there must be no alternative that achieves the same or comparable benefits with less harm or risk",
         "B. Those affected by technology should understand and accept the risks",
         "C. The benefits and burdens of technology should be distributed fairly. Those who benefit should bear their fair share of the risks, and those who do not benefit should not suffer a significant increase in risk",
         "D. Even if judged acceptable by the other guidelines, the technology must be implemented so as to avoid all unnecessary risks"]
     ),
    (
        "One of the major principles of technology ethics is that even if judged acceptable by the other three guidelines, the technology must be implemented so as to avoid all unnecessary risk. This principle is:",
        ["A. Informed consent",
         "B. Justice",
         "C. Minimized risk",
         "D. Proportionality"]
    ),
    (
        "All of the following are AITP standards of professional conduct related to a person's obligation to society except:",
        ["A. Protect the privacy and confidentiality of all information entrusted to me",
         "B. To the best of my ability, ensure that the products of my work are used in a socially responsible way",
         "C. Never misrepresent or withhold information that is germane to a problem or a situation of public concern",
         "D. Do not use knowledge of a confidential or personal nature in any unauthorized manner to achieve personal gain"]
    ),
    ("___ is/are the most commonly used security technology at large companies.",
     ["A. Intrusion-detection systems",
      "B. Smart cards",
      "C. Biometrics",
      "D. Antivirus software"]
     ),
    (
        "According to the text, all of the following statements are included in the definition of computer crime except:",
        ["A. Unauthorized modification of software, data, or network resources",
         "B. Unauthorized release of information",
         "C. Unauthorized copying of software",
         "D. Unauthorized distribution of public domain software"]
    ),
    ("According to the text, companies are protecting themselves from computer crime by using:",
     ["A. Antivirus software",
      "B. Intrusion-detection systems",
      "C. Biometrics",
      "D. All of the choices are correct."]
     ),
    (
        "___ means getting access to a computer system, reading some files, but neither stealing nor damaging anything.",
        ["A. Electronic breaking and entering",
         "B. Sniffing",
         "C. Snooping",
         "D. Dumpster diving"]
    ),
    (
        "The text defines ___ as the obsessive use of computers, or the unauthorized access and use of networked computer systems.",
        ["A. hacking",
         "B. cyber-slacking",
         "C. cracking",
         "D. resource theft"]
    ),
    (
        "The text defines a ___ as a person who maintains knowledge of the vulnerabilities he or she finds and exploits them for private advantage, not revealing them to either the general public or the manufacturer for correction.",
        ["A. hacker",
         "B. cyber-slacking",
         "C. cracker",
         "D. resource theft"]
    ),
    (
        "Hammering a Web site's equipment with too many requests for information, slowing performance or even crashing the site is called:",
        ["A. A logic bomb",
         "B. Denial of service",
         "C. A back door",
         "D. Social engineering"]
    ),
    (
        "Sifting through a company's garbage looking for information to help break into the company's computers; sometimes used in conjunction with social engineering is called:",
        ["A. Dumpster diving",
         "B. Denial of service",
         "C. A back door",
         "D. A sniffer"]
    ),
    ("Talking unsuspecting company employees out of valuable information such as passwords is called:",
     ["A. Sniffing",
      "B. Denial of service",
      "C. A back door",
      "D. Social engineering"]
     ),
    ("A ___ is software that can guess passwords.",
     ["A. logic bomb",
      "B. password cracker",
      "C. back door",
      "D. sniffer"]
     ),
    (
        "One way hackers gain access to an individual's information is by faking an e-mail address or Web page to trick users into passing along critical information like credit card numbers. This is known as ___.",
        ["A. sniffing",
         "B. hacking",
         "C. phishing",
         "D. spoofing"]
    ),
    ("According to the text case, ___ of people have stolen key information from work.",
     ["A. 10%",
      "B. 20%",
      "C. 70%",
      "D. 80%"]
     ),
    (
        "According to the text, companies can use ___ to attack the problem of unauthorized use of computer systems and networks, to monitor network traffic in order to reveal evidence of improper use.",
        ["A. sniffers",
         "B. snoopers",
         "C. zombies",
         "D. password crackers"]
    ),
    ("To use public domain software legally, a company:",
     ["A. Must purchase individual copies or a site license for a certain number of copies",
      "B. Can examine a single copy of the software for 30 days and then purchase as many copies as needed",
      "C. Can make as many copies as desired because the software is not copyrighted",
      "D. None of the choices are correct."]
     ),
    ("Software that is not copyrighted is called:",
     ["A. Shareware",
      "B. Open source",
      "C. Public domain",
      "D. None of the choices are correct."]
     ),
    ("All of the following are common ways for a computer virus to enter a computer system except:",
     ["A. E-mail and file attachments",
      "B. Running antivirus programs",
      "C. Downloaded copies of shareware",
      "D. Borrowed copies of software"]
     ),
    ("Which of the following statements about adware and spyware is true?",
     [
         "A. Protecting against this software usually requires the purchase and installation of programs designed to prevent the software from being downloaded and installed",
         "B. Removal programs are 100% successful, although they are very expensive",
         "C. Adware software removes spyware software from a user's computer",
         "D. A user must approve the downloading of adware, even if tricked into doing so"]
     ),
    (
        "Governments around the world are debating privacy issues and considering various forms of legislation. One area central to the privacy debate is opt-in versus opt-out. Those preferring the opt-in standard do so because this standard would:",
        ["A. Make privacy the default for consumers",
         "B. Make privacy the default, if a consumer calls in to request no data sharing",
         "C. Make sharing private information the default",
         "D. It would match the existing policy of most Internet-based companies"]
    ),
    (
        "Individuals have been mistakenly arrested and jailed, and others have been denied credit because of their physical profiles or personal data. These are often the result of:",
        ["A. Computer profiling and computer matching",
         "B. Unauthorized opt-in",
         "C. Censorship",
         "D. Adware"]
    ),
    ("Indiscriminate sending of unsolicited e-mail messages to many Internet users is called ___.",
     ["A. flaming",
      "B. spamming",
      "C. spoofing",
      "D. spying"]
     ),
    ("Sending extremely critical, derogatory, and often vulgar e-mail messages is called ___.",
     ["A. flaming",
      "B. spamming",
      "C. spoofing",
      "D. spying"]
     ),
    ("Computer monitoring has been criticized as unethical because:",
     ["A. It only monitors the work being done",
      "B. Nobody is overseeing the person doing the monitoring",
      "C. It is outside human control",
      "D. It monitors individuals, not just the job"]
     ),
    ("Computer monitoring has been criticized as an invasion of employee privacy because:",
     ["A. Many times employees do not know they are being monitored",
      "B. Employees know how the information is being used",
      "C. It monitors the work being done",
      "D. It is outside human control"]
     ),
    (
        "Information technologies have caused a significant reduction in the following types of job opportunities, except:",
        ["A. Accounting",
         "B. Control of machine tools",
         "C. E-commerce directors",
         "D. All the answers are jobs that have been reduced by information technologies"]
    ),
    ("Lawsuits by monitored workers against employers are:",
     ["A. increasing",
      "B. decreasing",
      "C. staying the same",
      "D. no longer permitted in any of the 50 states"]
     ),
    (
        "Which of the following is not a health issue commonly related to the use of information technology in the workplace?",
        ["A. Damaged arm and neck muscles",
         "B. Eyestrain",
         "C. Job stress",
         "D. Hearing loss"]
    ),
    (
        "People who sit at PC workstations or visual display terminals in fast-paced, repetitive-keystroke jobs can suffer from a variety of health problems, known collectively as ___.",
        ["A. Computer trauma disorders",
         "B. Eyestrain",
         "C. Carpal tunnel distress",
         "D. Cumulative trauma disorders"]
    ),
    ("Good ergonomic design considers tools, tasks, the workstation, and ___.",
     ["A. the users",
      "B. the environment",
      "C. the software",
      "D. previous injuries"]
     ),
    ("The goal of ergonomics is to design:",
     ["A. Effective work environments that are conducive to fast-paced, repetitive jobs",
      "B. Efficient work environments that are productive and promote high morale",
      "C. Healthy work environments that are safe, comfortable, and pleasant for people to work in",
      "D. Policies regarding work environment structures"]
     ),
    (
        "The text describes a/an ___ as a gatekeeper system that protects a company's intranets and other computer networks from intrusion by providing a filter and safe transfer point for access to and from the Internet and other networks.",
        ["A. firewall",
         "B. filtered portal",
         "C. encoder",
         "D. telecommunications line"]
    ),
    ("What is the purpose of external firewalls?",
     ["A. To prevent users from accessing sensitive human resource or financial data",
      "B. To limit access of intranet resources to specific users",
      "C. To avoid creating security holes to back-end resources",
      "D. To keep out unauthorized Internet users from intranet networks"]
     ),
    (
        "Firewall software has become essential for individuals connecting to the Internet with DSL or cable modems:",
        ["A. Because of their faster download speeds",
         "B. Because of their always on connection status",
         "C. Because antivirus software is not made for these connections",
         "D. All the choices are correct"]
    ),
    (
        "Which of the following is not a method used to defend against denial of service attacks at zombie machines?",
        ["A. Set and enforce security policies",
         "B. Monitor employee emails",
         "C. Remind users not to open .exe mail attachments",
         "D. Close unused ports"]
    ),
    (
        "In 2000, hackers broke into hundreds of servers and planted Trojan horse .exe programs, which were then used to launch a barrage of service requests in a concerted attack at e-commerce websites, such as Yahoo! and eBay. This is an example of a distributed ___ attack.",
        ["A. acceptance of service",
         "B. denial of service",
         "C. zombie",
         "D. Trojan virus"]
    ),
    (
        "Which of the following is a method used to defend against denial of service attacks at the victim's website?",
        ["A. Create backup servers and network connections",
         "B. Limit connections to each server",
         "C. Install multiple intrusion-detection systems and multiple routers for incoming traffic to reduce choke points",
         "D. All of the choices are correct."]
    ),
    ("Security monitors can control the use of all the following except:",
     ["A. Hardware",
      "B. Software",
      "C. External networks",
      "D. Data resources"]
     ),
    ("According to the text, backup files:",
     ["A. Are duplicate files of data or programs",
      "B. Can be used to reconstruct the original files if they are destroyed",
      "C. May be stored off-premises, sometimes in special storage vaults in remote locations",
      "D. All of the choices are correct."]
     ),
    ("According to the text, GIGO stands for:",
     ["A. Generalized input, gross output",
      "B. Gateway input, gateway output",
      "C. Gigabytes in, gigabytes out",
      "D. Garbage in, garbage out"]
     ),
    ("An effective disaster recovery plan would include which of the following?",
     [
         "A. Arrangements with other companies for use of alternative facilities as a disaster recovery site.",
         "B. A listing of what hardware, software, and facilities will be used.",
         "C. A listing of which applications will be processed, and in what priority.",
         "D. All of the choices are correct."]
     ),
    (
        "Within an organization, managing the business/IT planning process so that IT is aligned with strategic business goals is the responsibility of:",
        ["A. The CIO",
         "B. Both the CIO and the CEO",
         "C. Both the CTO and the CEO",
         "D. Both the CIO and the CSO"]
    ),
    (
        "Within an organization, managing the development and implementation of new business/IT applications and technologies is the responsibility of:",
        ["A. The CIO",
         "B. Both the CIO and the CEO",
         "C. Both the CTO and the CEO",
         "D. Both the CIO and the CTO"]
    ),
    (
        "CIO and IT managers share responsibility for managing the work of IT professionals. In addition, they are responsible for managing the:",
        ["A. Hardware infrastructure",
         "B. IT infrastructure of hardware, software, databases, and telecommunications networks",
         "C. IT infrastructure of hardware and software",
         "D. IT infrastructure of hardware, software, and human resources"]
    ),
    ("All of the following changes have created an urgent need for centralization except:",
     ["A. The Internet boom inspired businesses to connect to multiple networks",
      "B. Companies put essential applications on their intranets, without which their businesses could not function",
      "C. Maintaining PCs on a network is very, very expensive",
      "D. The number of qualified software programmers and PC repair technicians is dwindling"]
     ),
    (
        "The decentralization of information services within an organization was prompted by which of the following?",
        ["A. The development of supercomputers",
         "B. The development of microcomputers and distributed client/server networks at the corporate, department, and workgroup level",
         "C. The development of mainframe computers and centralized computer centers",
         "D. The development of telecommunications"]
    ),
    ("The development of minicomputers and microcomputers accelerated which of the following trends?",
     ["A. Centralization of computer hardware and software",
      "B. Downsizing",
      "C. Strategic planning",
      "D. Development of web portals"]
     ),
    ("Systems integrators or facilities management companies are:",
     [
         "A. Independent subsidiaries of an organization that offer information-processing services to external organizations, as well as to their parent company",
         "B. Companies that use information resource management techniques to manage the development of their information systems",
         "C. Outside contractors that take over part or all of a company's information services operations",
         "D. Companies using a hybrid of centralized and decentralized information systems."]
     ),
    (
        "According to the text, ___ is a key IT management responsibility if business/IT projects are to be completed on time, within budget, and meet design objectives.",
        ["A. hardware selection",
         "B. network vulnerability",
         "C. project management",
         "D. employee recruiting and development"]
    ),
    (
        "IS operations are a cost to the company. When a company uses system performance monitors and then allocates costs to user departments based on the information services rendered, the company is applying a(n) ___ system.",
        ["A. record keeping",
         "B. outsourcing",
         "C. chargeback",
         "D. rebound"]
    ),
    ("All of the following are common functions of a system performance monitor except:",
     ["A. Capturing computer operator keystrokes",
      "B. Looking after the processing of computer jobs",
      "C. Helping to develop a schedule of computer operations that can optimize computer system performance",
      "D. Producing detailed statistics that are used for planning and control"]
     ),
    ("All of the following are components of IT staff planning except:",
     ["A. Setting salary and wage levels",
      "B. Recruiting and retaining qualified personnel",
      "C. Determining pay periods",
      "D. Evaluating job performance"]
     ),
    ("A chief information officer (CIO):",
     ["A. Directs day-to-day information services activities",
      "B. Develops and administers training programs for information services personnel and computer users",
      "C. Is expected to closely supervise the internal operations of the information services department, but has limited responsibility for interfacing with other departments",
      "D. Has major responsibility for long-term information system planning and strategy"]
     ),
    ("The chief information officer is a(n) ___ level IT manager.",
     ["A. tactical",
      "B. strategic",
      "C. operational",
      "D. departmental"]
     ),
    (
        "According to the text, if you are second-in-command to the CIO or chief technology officer and have years of applications development experience, your next promotion should be to:",
        ["A. COO",
         "B. CEO",
         "C. CIO",
         "D. CTO"]
    ),
    ("In many companies, technology management is the primary responsibility of the:",
     ["A. COO",
      "B. CEO",
      "C. CIO",
      "D. CTO"]
     ),
    (
        "The ___ has a strong understanding of the issues related to protecting the data resources and information assets of the organization.",
        ["A. COO",
         "B. CSO",
         "C. CIO",
         "D. CTO"]
    ),
    (
        "The ___ has problem-solving skills and a degree in information systems, excellent interpersonal skills, good technical skills, and an ability to apply problem-solving and critical-thinking skills to the design of new systems.",
        ["A. Systems analyst",
         "B. Practice manager",
         "C. CIO",
         "D. Team leader"]
    ),
    (
        "Many companies have created ___ functions to support and manage end-user and workgroup computing.",
        ["A. customer relationship managers",
         "B. information centers",
         "C. user services",
         "D. end-user focus groups"]
    ),
    (
        "The ___ usually knows Java, Perl, C++, and Web services. He/she also has experience in systems architecture, and can design an Internet solution from concept through implementation.",
        ["A. e-commerce architect",
         "B. practice manager",
         "C. systems analyst",
         "D. chief technology officer"]
    ),
    ("Many people are employed in IT in a large company. A technical team leader would:",
     ["A. Be second in command to the CIO",
      "B. Know Java, Perl, and Web services, and possess the ability to design an Internet solution from concept through implementation",
      "C. A senior member of the technical team and has good communication, leadership, and project management skills",
      "D. Have skills in marketing, staffing, budgeting, and building customer relationships"]
     ),
    (
        "All of the following were listed in the text as primary reasons behind a company's decision to outsource except:",
        ["A. Achieving a greater return on investment",
         "B. Achieving flexible staffing levels",
         "C. Focusing on core competencies",
         "D. Centralizing software development"]
    ),
    ("Which of the following is the number one reason that companies outsource?",
     ["A. Reduce and control operating costs",
      "B. Accelerate re-engineering benefits",
      "C. Gain access to world-class capabilities",
      "D. Share risks"]
     ),
    ("What is the number one factor for successful outsourcing?",
     ["A. Reducing and controlling operating costs",
      "B. Understanding the company's goals and objectives",
      "C. Commitment to quality",
      "D. Sharing the risks"]
     ),
    ("What is the number one factor for successful selection of an outsourcing vendor?",
     ["A. Senior executive support and involvement",
      "B. Gaining access to world-class capabilities",
      "C. Commitment to quality",
      "D. Sharing risks"]
     ),
    ("What is the number one IT area being outsourced?",
     ["A. Client/server services and administration",
      "B. Applications development",
      "C. End-user support",
      "D. Maintenance and repair"]
     ),
    ("All of the following are among the top 10 factors in vendor selection except:",
     ["A. Commitment to quality",
      "B. Price",
      "C. End-user support",
      "D. Cultural match"]
     ),
    ("Which of the following is the least outsourced IT area?",
     ["A. Maintenance and repair",
      "B. Consulting and re-engineering",
      "C. Network administration",
      "D. Total IT outsourcing"]
     ),
    ("The text defines offshoring as:",
     [
         "A. Relocation of an organization's business processes to a lower-cost location, usually overseas",
         "B. Relocation of an organization's business processes to another firm better qualified to handle those processes",
         "C. Relocation of an organization's production, but not services, to a lower-cost location",
         "D. Complete and total IT outsourcing"]
     ),
    ("The text distinguishes between two types of offshoring:",
     ["A. Domestic and international",
      "B. Production and services",
      "C. Complete and partial",
      "D. Internal and external"]
     ),
    (
        "Senior management needs to be involved in critical business/IT decisions. Which of the following is not such a decision?",
        ["A. What security and privacy risks are acceptable?",
         "B. How good do our IT services need to be?",
         "C. Which hardware platform do we centralize on?",
         "D. Who do we blame if an IT initiative fails?"]
    ),
    (
        "Many companies have policies that require managers to be involved in IT decisions that affect their business units. This helps managers:",
        ["A. Improve the strategic customer value of information technology",
         "B. Avoid IS performance problems in their business units and development projects",
         "C. Monitor the problems of employee resistance and poor user interface design",
         "D. See other opportunities for IT development"]
    ),
    (
        "When a company experiences excessive technical and process standardization that limit the flexibility of business units, or frequent exceptions to the standards that increase costs and limit business synergies, this is often the result of senior management failing to answer the question:",
        ["A. Which IT capabilities should be companywide?",
         "B. How much should be spent on IT?",
         "C. Which business processes should receive our IT dollars?",
         "D. Whom should we blame if an IT initiative fails?"]
    ),
    (
        "When a company experiences a lack of focus, the IT unit can become overwhelmed as it tries to deliver many projects that may have little company-wide value or can't be implemented well simultaneously. This is often the result of senior management failing to answer the question:",
        ["A. Which IT capabilities should be companywide?",
         "B. How much should be spent on IT?",
         "C. Which business processes should receive our IT dollars?",
         "D. Whom should we blame if an IT initiative fails?"]
    ),
    (
        "What would senior management's role be in relation to the question Whom do we blame if an IT initiative fails?",
        [
            "A. Decide which IT capabilities should be provided centrally and which should be developed by individual businesses",
            "B. Decide which features are needed on the basis of their costs and benefits",
            "C. Lead the decision making on the trade-offs between security and privacy on one hand and convenience on the other",
            "D. Assign a business executive to be accountable for every IT project, and monitor business metrics"]
    ),
    (
        "What would senior management's role be in relation to the question What security and privacy risks will we accept?",
        [
            "A. Decide which IT capabilities should be provided centrally and which should be developed by individual businesses",
            "B. Lead the decision making on the trade-offs between security and privacy on one hand and convenience on the other",
            "C. Decide which features are needed on the basis of their costs and benefits",
            "D. Assign a business executive to be accountable for every IT project, and monitor business metrics"]
    ),
    ("The consequence of failing to establish how good IT services really need to be is:",
     [
         "A. The company may fail to develop an IT platform that furthers its strategy, despite high IT expenditures",
         "B. Excessive technical and process standardization limits the flexibility of business units",
         "C. IT is overwhelmed with projects that have little companywide value",
         "D. The company may pay for service options that, given its priorities, aren't worth the money"]
     ),
    ("What is the consequence of failing to answer the question, how much should be spent on IT?",
     [
         "A. The company may fail to develop an IT platform that furthers its strategy, despite high IT expenditures",
         "B. Excessive technical and process standardization limits the flexibility of business units",
         "C. IT is overwhelmed with projects that have little companywide value",
         "D. The company may pay for service options that, given its priorities, aren't worth the money"]
     ),
    ("According to the text, COBIT is:",
     ["A. A methodology for determining the political structure of each country for IT operations",
      "B. A popular methodology for developing complex global information systems",
      "C. A popular IT governance approach that focuses on all aspects of the IT function throughout the organization",
      "D. A method for evaluating the infrastructure capabilities for IT in the target country"]
     ),
    ("COBIT stands for:",
     ["A. Centralized Operations for Business Information Technologies",
      "B. Compressed Operational BITs (Binary Digits)",
      "C. Computerized Objectives and Internet Technologies",
      "D. Control Objectives for Information and related Technology"]
     ),
    (
        "According to the text case, all the following lessons were learned from the COBIT implementation at Blue Cross, except:",
        [
            "A. Building in the controls makes the controls easier to sustain and it makes self-testing more efficient and effective",
            "B. Developing appropriate controls should be left to the end users",
            "C. It is best to build the controls into the process",
            "D. If the controls are not built into the process, the area performing the self test may have to process data for a great many hours"]
    ),
    ("According to the text, we seem to have reached a point where virtually every CIO is a(n):",
     ["A. global CIO—a leader whose sphere of influence (and headaches) spans continents",
      "B. global enterprise leader, capable of developing appropriate business and IT strategies for the global marketplace",
      "C. global politician who takes on the cultural, political, and geoeconomic challenges that exist in the international business community",
      "D. global technical expert, evaluating the infrastructure of the target country, including telephone and electricity transmission capabilities"]
     ),
    ("According to the text, all global IT activities must be adjusted to take into account:",
     ["A. Determining the political structure of each country of operations",
      "B. Developing appropriate business and IT strategies for the global marketplace",
      "C. The cultural, political, and geoeconomic challenges that exist in the international business community",
      "D. Evaluating the infrastructure of the target country, including telephone and electricity transmission capabilities"]
     ),
    ("According to the text, the first step in global information technology management should be:",
     ["A. Determining the political structure of each country of operations",
      "B. Developing appropriate business and IT strategies for the global marketplace",
      "C. Outsourcing all manufacturing to the lowest-cost location",
      "D. Evaluating the infrastructure of the target country, including telephone and electricity transmission capabilities"]
     ),
    ("All of the following are major dimensions of global IT challenges except:",
     ["A. Global business and IT strategies",
      "B. Global business and IT application portfolios",
      "C. Global IT platforms",
      "D. Global software management"]
     ),
    ("All of the following would be associated with a transnational e-business strategy except:",
     ["A. Global e-commerce and customer service",
      "B. Global supply chain and logistics",
      "C. Transparent manufacturing",
      "D. Dissimilar systems and data"]
     ),
    ("All of the following would be associated with a global e-business strategy except:",
     ["A. Global sourcing",
      "B. Multiregional",
      "C. Transparent manufacturing",
      "D. Horizontal integration"]
     ),
    ("All of the following would be associated with an international e-business strategy except:",
     ["A. Captive manufacturing",
      "B. Global supply chain and logistics",
      "C. Specific customers",
      "D. Region specific"]
     ),
    ("Which of the following would be associated with an international e-business strategy?",
     ["A. Customer segmentation and dedication by region and plant",
      "B. Global supply chain and logistics",
      "C. Some cross regionalization",
      "D. Horizontal integration"]
     ),
    ("All of the following would be associated with a global e-business strategy except:",
     ["A. Some cross regionalization",
      "B. Global supply chain and logistics",
      "C. Customer segmentation and dedication by region and plant",
      "D. Horizontal integration"]
     ),
    ("Which of the following would be associated with a transnational e-business strategy?",
     ["A. Customer segmentation and dedication by region and plant",
      "B. Horizontal integration",
      "C. Some cross regionalization",
      "D. Global supply chain and logistics"]
     ),
    ("Which of the following is a business driver for global IT?",
     ["A. Unique assembly line hardware",
      "B. Isolated work unit software",
      "C. Global collaboration",
      "D. Regional employees"]
     ),
    ("Most multinational companies have all of the following except:",
     ["A. Global financial budgeting",
      "B. Satellite-based communication systems",
      "C. Office automation systems, such as fax and e-mail",
      "D. Global cash management systems"]
     ),
    ("Hardware choices are difficult in some countries because of ___.",
     ["A. high prices",
      "B. import restrictions",
      "C. lack of documentation tailored to local conditions",
      "D. All of the choices are correct."]
     ),
    ("All of the following are international network management issues except:",
     ["A. Prohibiting transborder data flow",
      "B. Improving the operational efficiency of networks",
      "C. Dealing with multiple networks",
      "D. Controlling data communication security"]
     ),
    (
        "By connecting their businesses to the online infrastructure of the Internet, companies can generally do all of the following except:",
        ["A. Expand their markets",
         "B. Reduce communications and distribution costs",
         "C. Improve their profit margins without massive outlays for new telecommunications facilities",
         "D. Reduce the number of direct competitors"]
    ),
    ("Which of the following world regions has the highest per capita Internet usage?",
     ["A. Asia",
      "B. Europe",
      "C. North America",
      "D. Latin America/Caribbean"]
     ),
    ("All of the following are U.S.-EU data privacy requirements except:",
     ["A. Notice of purpose and use of data collected",
      "B. Redundant hardware and data backup systems",
      "C. Access for consumers to their information",
      "D. Adequate security, data integrity, and enforcement provisions"]
     ),
    (
        "According to the text, many countries view the process of transborder data flows as violating their laws for all the reasons, except:",
        ["A. national sovereignty",
         "B. privacy legislation",
         "C. laws designed to protect the local IT industry from competition",
         "D. anti-terrorist security precautions"]
    ),
    (
        "According to the Reporters Without Borders organization, 45 countries restrict their citizen's Internet access. Which of the following countries allows no public access to the Internet?",
        ["A. China",
         "B. North Korea",
         "C. Cuba",
         "D. Saudi Arabia"]
    )
]


@app.route('/')
def homepage():

    return render_template("homepage.html",

                           q_id=random.randint(0, len(questions) - 1))


@app.route('/<q_id>')
def question(q_id):

    wrong = ["A", "B", "C", "D"]
    wrong.remove(answers[int(q_id)])

    return render_template("question.html",

                           question_text=questions[int(q_id)][0],
                           a=questions[int(q_id)][1][0],
                           b=questions[int(q_id)][1][1],
                           c=questions[int(q_id)][1][2],
                           d=questions[int(q_id)][1][3],
                           answer=answers[int(q_id)],

                           wrong_1=wrong[0],
                           wrong_2=wrong[1],
                           wrong_3=wrong[2],

                           next=random.randint(0, len(questions) - 1))


if __name__ == '__main__':
    app.run()
