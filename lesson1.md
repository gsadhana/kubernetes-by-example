# Problem 1: deploy an API to Kubernetes

{% capture questions %}
these are the questions
{% endcapture %}

{% capture objectives %}
{% endcapture %}

{% include goals.html %}

- questions 
    - how do I deploy an API to Kubernetes? 
    - what's the difference between a container, pod, replicaset, and deployment? 
- learning objectives
    - create a pod for your api using YAML and Kubectl 
    - deploy api to kubernetes using YAML 
- assessments
    - update yaml to deploy 4 instances of the api 
    - update yaml to run api on port 8001 
    - create yaml to deploy api packaged via containerd instead of docker 
    - quiz: pod deleted -- why didn't the pod restart automatically? 
    - quiz: wrong spacing in yaml 
    - quiz: wrong label in pod -- why didn't deployment find the pod 
    - quiz: port forward syntax (container port is 8000, pod port is 8001)
- lesson outline
    - api 
    - containers 
        - dockerfile 
        - package up application + dependencies 
    - pods 
        - smallest deployable unit in kubernetes 
        - abstraction around containers 
            - why not deploy containers directly? 
                - to avoid being tied to specific implementation pattern 
                - to be able to group related containers together 
        - yaml
            - human readable config files 
            - spacing is important
            - link to tutorial  
        - kubectl 
            - how to install 
            - how to connect to a kubernetes cluster 
            - how to run commands 
            - link to tutorial 
        - apply provided pod.yaml to create pod 
        - port-forward to open api locally
        - walk through pod.yaml 
            - metadata 
            - container specification 
            - port 
    - deployments
        - delete pod via kubectl 
        - api is down 
        - replica sets 
