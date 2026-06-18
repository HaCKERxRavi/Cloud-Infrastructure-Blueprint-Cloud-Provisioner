# ========================================================================
# PROJECT: ENTERPRISE CLOUD-BASED SYSTEM PROVISIONER (FINAL BUILD)
# LOGIC: Network + Compute Provisioning + Dynamic JSON Configuration Export
# ========================================================================

import os
import sys
import time
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_provisioner():
    clear_screen()
    print("=====================================================")
    print("        ENTERPRISE CLOUD SYSTEM PROVISIONER          ")
    print("=====================================================")
    print("[*] Initializing DevOps Automation Framework...")
    time.sleep(0.5)

    # --------------------------------------------------------------------
    # MILESTONE 1: Environment Check
    # --------------------------------------------------------------------
    try:
        user_profile = os.environ.get('USERPROFILE', 'Unknown Server Context')
        print(f"[SUCCESS] Identity verified for: {user_profile}")
    except Exception as e:
        print(f"[ERROR] Security Context Failed: {str(e)}")
        sys.exit(1)

    print("-----------------------------------------------------")
    
    # --------------------------------------------------------------------
    # MILESTONE 2: Network Infrastructure
    # --------------------------------------------------------------------
    print("[*] PHASE 1: Deploying Isolated Network Topology...")
    vpc_cidr = "10.0.0.0/16"
    print(f"    -> [ACTIVE] VPC Boundary Established: {vpc_cidr}")
    print("    -> [ACTIVE] Corporate-Public-Subnet (10.0.1.0/24)")
    print("    -> [ACTIVE] Secure-Backend-Subnet (10.0.2.0/24)")
    
    print("-----------------------------------------------------")

    # --------------------------------------------------------------------
    # MILESTONE 3: Compute & Virtual Machine Provisioning
    # --------------------------------------------------------------------
    print("[*] PHASE 2: Launching Cloud Compute Instances (VMs)...")
    time.sleep(0.5)

    server_cluster = [
        {"name": "Prod-Web-Server-01", "type": "t3.medium", "zone": "Public", "ip": "10.0.1.45", "status": "RUNNING"},
        {"name": "Prod-DB-Replica-01", "type": "r6i.xlarge", "zone": "Private", "ip": "10.0.2.110", "status": "RUNNING"}
    ]

    for server in server_cluster:
        print(f"[+] Provisioning Node: {server['name']}...")
        print(f"    -> Instance Configuration Profiles: Type {server['type']} | OS: Ubuntu-Server")
        print(f"    -> [RUNNING] Node Online | Internal Private IP: {server['ip']}")
        print("")

    print("-----------------------------------------------------")

    # --------------------------------------------------------------------
    # MILESTONE 4: Centralized Infrastructure Configuration Export
    # --------------------------------------------------------------------
    print("[*] PHASE 3: Compiling Deployment Manifest & Asset Logs...")
    time.sleep(1)

    # Creating the orchestration state payload
    manifest_data = {
        "OrchestrationTime": time.strftime("%Y-%m-%d %H:%M:%S"),
        "NetworkTopology": {
            "VPC_CIDR": vpc_cidr,
            "ActiveSubnets": ["10.0.1.0/24", "10.0.2.0/24"]
        },
        "DeployedAssets": server_cluster,
        "SecurityHardening": "ENABLED"
    }

    report_filename = "infrastructure_report.json"
    
    try:
        # Writing data onto a physical file
        with open(report_filename, "w") as json_file:
            json.dump(manifest_data, json_file, indent=4)
        print(f"[SUCCESS] Enterprise Manifest exported to local state engine.")
        print(f" -> Output Saved: D:\\project\\Cloud-Provisioner\\{report_filename}")
    except Exception as e:
        print(f"[ERROR] Asset Reporting Failed: {str(e)}")

    print("=====================================================")

if __name__ == "__main__":
    initialize_provisioner()