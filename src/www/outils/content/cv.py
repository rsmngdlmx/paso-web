# -*- coding: utf-8 -*-

'''
Copyright 2026. Created in Zapopan, Mexico. All Rights Reserved.
'''

__author__ = 'Ricardo Samuel Mendoza Núñez <rsmn.development@gmail.com>'
__status__ = 'Development'
__date__ = '23-05-2026'
__last_update__ = '23-05-2026'


from django.utils.translation import gettext_lazy as _

content = {
    'title': 'Curriculum Vitæ | Ricardo Mendoza',
    'summary': _("I'm a Software Engineer with over 15 years of experience as "
                'a Full Stack Developer. I have extensive experience '
                'developing REST APIs, microservices, and Serverless '
                'solutions. My work focuses on architecting and developing '
                'secure, efficient, and scalable applications using mainly '
                'JavaScript and Python, as well as deploying them to cloud '
                'providers like AWS and Azure. I recently began '
                'incorporating AI throughout the SDLC to boost development '
                'speed and improve the quality of the software.'),
    'skills': _('Technical skills'),
    'prog_lang': _('Programming languages'),
    'databases': _('Databases'),
    'work_exp': _('Professional experience'),
    'april': _('Apr'),
    'may': _('May'),
    'july': _('Jul'),
    'september': _('Sep'),
    'october': _('Oct'),
    'november': _('Nov'),
    'december': _('Dec'),
    'present': _('Currently working here'),
    'fullstack': _('Full Stack Developer'),
    'techlead': _('Tech Lead'),
    'backend': _('Back End Developer'),
    'dot_net_dev': _('.NET Developer'),
    'mobile_dev': _('iOS/Android Developer'),
    'tech_support': _('Technical Support'),
    'ms_intern': _('Microsoft Intern'),
    'gov': _('Government of the State of Jalisco (CGIG)'),
    'udg': _('University of Guadalajara'),
    'recognition': _('Recognition'),
    'w9_p1': _('In charge of the tech transition of several stacks from <span '
                'class="txt-bold">.NET</span> to <span class="txt-bold">'
                'Node.js</span> to help reduce infrastructure costs while '
                'improving the performance and scalability of the stacks. '
                'Deployed the stacks to <span class="txt-bold">AWS Lambda'
                '</span>, <span class="txt-bold">ECS</span>, and <span '
                'class="txt-bold">EKS</span> services using <span '
                'class="txt-bold">Terraform</span> and <span class="txt-bold">'
                'Harness</span>.'),
    'w9_p2': _('Contributed to the development of several web components '
                'made with <span class="txt-bold">Vanilla JavaScript</span>. '
                'The web components helped standardize the UI/UX throughout '
                "the website of one of Altimetrik's clients."),
    'w8_p1': _('Led the development team to successfuly '
                'achieve the technical goals of the company.'),
    'w8_p2': _('Developed a chatbot for converting leads into customers '
                'through social channels like Facebook Messenger and '
                'WhatsApp. The chatbot helped increase leads conversion by '
                '26%. It was developed using <span class="txt-bold">Node.js'
                '</span>, <span class="txt-bold">MySQL</span>, <span '
                'class="txt-bold">PostgreSQL</span> and <span '
                'class="txt-bold">MongoDB</span>.'),
    'w8_p3': _("Contributed to the development of the company's CRM "
                'using <span class="txt-bold">Node.js</span>, <span '
                'class="txt-bold">AWS Lambda</span>, <span class='
                '"txt-bold">MySQL</span>, <span class="txt-bold">PostgreSQL'
                '</span> and <span class="txt-bold">React</span>.'),
    'w7_p1': _('Developed microservices using <span class="txt-bold">Node.js'
                '</span> and <span class="txt-bold">GraphQL</span> and '
                'deployed them to <span class="txt-bold">AWS Lambda</span>.'),
    'w7_p2': _('Implemented a <span class="txt-bold">Headless CMS (Webiny)'
                '</span> to dynamically serve localized content for a '
                'website, improving loading times by nearly 30%.'),
    'w6_p1': _('Built web applications using a client-server architecture '
                'with <span class="txt-bold">Angular</span> in the front end '
                'and <span class="txt-bold">Lumen (PHP)</span> in the back '
                'end. Developed backend services with an MVC architecture '
                'using <span class="txt-bold">Laravel (PHP)</span> connected '
                'to <span class="txt-bold">MySQL</span> and <span '
                'class="txt-bold">PostgreSQL</span> databases.'),
    'w6_p2': _('Developed a backend management system for a Government '
                'department using <span class="txt-bold">Django (Python)'
                '</span> and <span class="txt-bold">PostgreSQL</span> to help '
                'increase productivity by automating several processes of the '
                'department.'),
    'w6_p3': _('Collaborated on building a mobile app for a social program '
                'using the <span class="txt-bold">Ionic</span> framework.'),
    'w5_p1': _('Worked on the REST APIs that constituted '
                'the booking engine of the airline using <span '
                'class="txt-bold">C#</span>, <span class="txt-bold">ASP.NET '
                'MVC</span> and <span class="txt-bold">ASP.NET Core</span>.'),
    'w5_p2': _("In charge of the integration of the airline's booking engine "
                'with some of the major booking brokers like Expedia, '
                'SkyScanner, and Despegar, resulting in a considerable boost '
                "on the airline's sales."),
    'w5_p3': _('Collaborated on configuring and managing virtual servers and '
                'cloud services on <span class="txt-bold">Azure</span>.'),
    'w4_p1': _('Designed, architected, and developed a MOOC platform based on '
                'Open edX. It was built with <span class="txt-bold">Django '
                '(Python)</span> and <span class="txt-bold">Flask (Python)'
                '</span> and deployed on a private server with <span '
                'class="txt-bold">Debian</span> and <span class="txt-bold">'
                'Nginx</span>.'),
    'w3_p1': _('Led the development of CARES, a healthcare project that won '
                'the first place on the international contest FI-WARE Smart '
                'Society (october 2014) and was amongst the finalists of the '
                'internatinoal contest FI-WARE Smart Cities (january 2014).'),
    'w3_p2': _('Developed web services with <span class="txt-bold">Tornado '
                '(Python)</span>.'),
    'w3_p3': _('Built productivity apps for iOS and Android using <span '
                'class="txt-bold">Objective-C</span> and <span '
                'class="txt-bold">Java</span>.'),
    'w3_p4': _('Collaborated on the development of videogames for iOS using '
                '<span class="txt-bold">Objective-C</span> and <span '
                'class="txt-bold">Cocos 2D</span>.'),
    'w2_p1': _('In charge of the computerization of the institution.'),
    'w2_p2': _('Built a desktop application to help manage the library of the '
                'institution with <span class="txt-bold">.NET (C#)</span> '
                'and <span class="txt-bold">MySQL</span>.'),
    'w1_p1': _('Contributed to the development of a desktop application to '
                'monitor UDGLive@edu accounts using <span class="txt-bold">'
                '.NET (C#)</span> and <span class="txt-bold">Oracle</span>.'),
    'edu_title': _('Education'),
    'deg_title': _('Computer Engineering'),
    'certs_title': _('Certifications'),
    'verification_link': _('Verification link'),
    'personal_projects': _('Personal projects'),
    'personal_website': _('Personal website'),
    'p1_p1': _('Website developed with <span class="txt-bold">Django '
                '(Python)</span> and deployed on a <span class="txt-bold">Web '
                'App</span> on <span class="txt-bold">Azure</span>.'),
    'p2_p1': _('Website developed with <span class="txt-bold">Django '
                '(Python)</span> and deployed on a <span class="txt-bold">Web '
                'App</span> on <span class="txt-bold">Azure</span>.'),
    'languages': _('Languages'),
    'native': _('native'),
    'english': _('English'),
    'spanish': _('Spanish'),
    'french': _('French'),
    'japanese': _('Japanese'),
    'german': _('German'),
}
