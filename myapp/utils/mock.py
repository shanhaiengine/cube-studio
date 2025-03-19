import copy
import random
import string
from datetime import datetime, timedelta

def get_time(num):
    now = datetime.now()
    one_day_ago = now - timedelta(days=num)
    return one_day_ago.strftime("%Y-%m-%d %H:%M:%S")

def get_str(num):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.sample(characters, k=num))

def mock_data1(num):
    result = {}
    sample = {
            "cpu": 2,
            "memory": 768,
            "labels": {
            "beta.kubernetes.io/arch": "amd64",
            "beta.kubernetes.io/os": "linux",
            "cpu": "true",
            "istio": "true",
            "kubeflow": "true",
            "kubeflow-dashboard": "true",
            "kubernetes.io/arch": "amd64",
            "kubernetes.io/hostname": "172.16.13.50",
            "kubernetes.io/os": "linux",
            "logging": "true",
            "monitoring": "true",
            "mysql": "true",
            "node-role.kubernetes.io/controlplane": "true",
            "node-role.kubernetes.io/etcd": "true",
            "node-role.kubernetes.io/worker": "true",
            "notebook": "true",
            "org": "public",
            "redis": "true",
            "service": "true",
            "train": "true"
            },
            "name": "172.16.13.50",
            "create_time": "2025-02-25 12:07:28",
            "node_info": {
            "architecture": "amd64",
            "boot_id": "fa0a0038-2406-4e9d-b1d3-af55d8b91596",
            "container_runtime_version": "docker://27.4.1",
            "kernel_version": "5.15.0-130-generic",
            "kube_proxy_version": "v1.25.16",
            "kubelet_version": "v1.25.16",
            "machine_id": "71a01ddc75484a7ea6a79e1372cfeac1",
            "operating_system": "linux",
            "os_image": "Ubuntu 22.04.4 LTS",
            "system_uuid": "5ec4c29c-46de-03e5-0010-debf6060f071"
            },
            "status": "Ready",
            "gpu": 0,
            "hostip": "172.16.13.50",
            "used_memory": 9,
            "used_cpu": 6,
            "used_gpu": 0
        }
    
    index = 0
    while index < num:
        index += 1
        label = "192.168.1." + str(10+index)
        
        data = copy.deepcopy(sample)
        data["create_time"]= get_time(2)
        data["kubernetes.io/hostname"] = label
        data["name"] = label
        data["hostip"] = label
        result[label] = data
    return result
    
def mock_data2(num):
    result = []
    models = ['volcano','yolov7','nlp-process','jina-embeddings','bge-reranker-v2-m3']
    sample = {
        'cluster': 'prd',
        'project': 'HTY',
        'resource_group': 'public',
        'namespace':'service',
        'pod':'volcano-20250101-75459d00r2-abcde',
        'pod_info': 'prd:service:public:volcano-20250101-75459d00r2-abcde',
        'label': {
            'app': 'volcano-20250101',
            'pod-template-hash': '75459d47d9',
            'pod-type': 'inference',
            'user': 'admin'
        },
        'username': 'admin',
        'node': '172.16.13.51',
        'cpu': '1/2',
        'memory': '1/12',
        'gpu': '2.0',
        'start_time': '2025-02-24 12:00:28'
    }

    index = 0
    while index < num:
        index += 1
        label = "192.168.1." + str(10+index)
        model = random.choices(models, k=1)[0]
        
        data = copy.deepcopy(sample)
        pod_template_hash = str(get_str(10))

        data["pod"] = model +  "-20250101-" + pod_template_hash + "-" + get_str(5)
        data["pod_info"] = "prd:service:public:" + data["pod"]
        data["label"]["app"] = model + "-20250101"
        data["label"]["pod-template-hash"] = pod_template_hash
        data["node"] = label
        data["cpu"] = str(random.randrange(1, 3)) + '/2'
        data["memory"] = str(random.randrange(6, 13)) + '/12'
        data["start_time"]= get_time(2)

        result.append(data)
    return result

def mock_data3():
    all_resource = {'mem_all': 150, 'cpu_all': 400, 'gpu_all': 1600}
    all_resource_req = {
        'mem_req': round((0.5 + random.random() * 0.5) * all_resource["mem_all"]), 
        'cpu_req': round((0.5 + random.random() * 0.5)  * all_resource["cpu_all"]), 
        'gpu_req': round((0.5 + random.random() * 0.5)  * all_resource["gpu_all"]), 
    }
    all_resource_used = {
        'mem_used': round((0.5 + random.random() * 0.5)  * all_resource["mem_all"]), 
        'cpu_used': round((0.5 + random.random() * 0.5)  * all_resource["cpu_all"]), 
        'gpu_used': round((0.5 + random.random() * 0.5)  * all_resource["gpu_all"]), 
    }
    return {
        "all_resource": all_resource,
        "all_resource_req": all_resource_req,
        "all_resource_used": all_resource_used
    }
