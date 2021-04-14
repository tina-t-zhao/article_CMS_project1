# Write-up 

### Analyze, choose, and justify the appropriate resource option for deploying the app.

* Compare a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- VM is a infrastructure as a service(IaaS), have full control over computing environment while Web app is a platform as a service(Paas), which allows to integrate without managing the underlying infrasture
- Costs: Pricing for VM examples: Burstable VMs B1S: $0.008/hour, compute optimized Fsv2: $0.085/hour, general purpose Dv4:$0.096/hour, memory optimized Ev4: $0.126/hour. Pricing for web app is not listed on the website, but there are free and preview plans to test apps within budget, and there are basic, standard and premium plans for production workloads. Pay as you go price is free for Free try for free, $0.013/hour for shared environment for dev/test, $0.075/hour for dedicated environment. So it seems web app is a little more expensive. But for our small app, it costs nothing.
- Scalability: Autoscaling is built-in service in App service while VM scale sets supports autoscaling in VM
- Workflow: In general, there is a tradeoff between control and ease of management. IaaS gives the most control, flexibility, and portability, but you have to provision, configure and manage the VMs and network components you create. FaaS services automatically manage nearly all aspects of running an application. PaaS services fall somewhere in between.

### Choose the appropriate solution (VM or App Service) for deploying the app*
  I choose web app service over VM because of the following reasons:
  Secure web app development
  Versatile framework that it provide support for ASP.NET, Node.js, Java, Python and PHP
  Scalibility with availability
  Visual studio integration
  Analytics and log stream,that it provides a detailed view of appliaction health and performance.
  Extensive list of application templates

### Assess app changes that would change your decision.

Just like discussed above, there's a tradeoff between control and ease of management. When the app needs to scale up and I have to take more control of my infrastructure such as memory, operating system, storage etc, then VM would be a better choice to have better efficiency.
