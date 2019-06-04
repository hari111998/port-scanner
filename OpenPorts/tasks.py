from PortScanner.celery import app
from .models import Scan
from celery.signals import worker_process_init
from multiprocessing import current_process
from django.shortcuts import render
from random import randint
from py_port_scan import MultiScan


@app.task
def scanOpenPorts(ips, ports, threads, timeout, username, password):

    res = {}

    mulScan = MultiScan(targets=ips, ports=range(ports[0], ports[1]),
                        threads=threads, timeout=timeout)

    res["ips"] = dict(mulScan.run_full_scan())
    res["total_runtime"] = round(mulScan.get_total_runtime(), 2)
    res["id"] = "".join([chr(randint(65, 65+25)) for x in range(20)])
    res["ports"] = str((ports[1] - ports[0])*len(ips))

    user_id = str(username) + str(password)

    scan = Scan(user_id=user_id, data=str(res))
    scan.save()