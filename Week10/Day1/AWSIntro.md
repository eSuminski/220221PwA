# AWS
In recent years, Amazon Web Services (AWS) has blown up in popularity, spawning many similar styles of web service providers. There are many benfits for a company to use AWS and/or other web service providers; here are 6 key benefits to using their services:
1. Trade capital expense for variable expense
    - Instead of needing to guess at your traffic and processing needs you can use a flexible service that scales (both up and down) to your needs. This allows you as a company to focus on developing your product, not your IT infastructure
2. Benefit from massive economies of scale
    - because user actions are all aggregated in the cloud you can benefit from a pay-as-you-go model that many web service providers like AWS offer. 
3. You don't have to guess what your capacity is
    - similar to the first two bullet points, you no longer need to guess at what your hardware requirements are going to be: the autoscaling offered by AWS means you won't be sitting on unnecessary hardware during business lulls, and on the flip-side, if your business gets more traffic than you were expecting, you don't have to worry about a limited amount of hardware ruining your users' experiences.
4. Increased speed and agility
    - When you host a service locally you have to manually upgrade/adujust things (wheter it is a new software update, changing OS, etc.). If your systems are in the cloud, however, all you have to do is change a few settings and your system is updated/migrated to a new version/OS/whatever change you need to make. This is the potential difference between hours-weeks lost and a few minutes, mabye a few hours at most lost. 
5. Eliminate overhead costs of maintaining data centers
    - AWS and other web service providers handle the maintanence of data centers, which means you can focus on your product
6. You can go global in minutes
    - because most services like AWS have global coverage, you can choose where you want to deploy your application and reduce the latency that your users will experience. Thiss allows you to have a global product in minutes, whereas in the past this would take multiple years to set up

### Models of Cloud Computing
- Infastructor as a service (IaaS)
    - a self-service model for managing remote data center infastructor. AWS offers IaaS in the form of data centers. In a sense, AWS is itself the IaaS.
    - key take-away: AWS provides IaaS via its data centers
- Platform as a service (PaaS)
    - allows organizations to build. run, and manage applications without the IT infastructure that is normally necessary. An example of this is AWS's RDS: it provides the means of managing your product (storing data related to it) without providing the infastructure to manage it(you need something like Dbeaver to set up your database, and you need an application to interface and use your database provided by Amazon).
    - key take-away: amazon provides tools, you must provide means of interacting with the tool
- Software as a service (SaaS)
    -  this replaces the traditional on-device software with software that is liscened on a subscription basis. It is centrally hosted in the cloud and interfaced with via a browser. Salesforce is a good represntation of this.