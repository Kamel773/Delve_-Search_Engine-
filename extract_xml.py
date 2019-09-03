import subprocess
import os
from multiprocessing import Pool
import tqdm
import random
import glob

def extract_xml(paper_path):
    servers = ["localhost", "10.68.202.199", "10.68.202.156"]
    server = servers[0]#random.randint(0,2)]
    try:
        command = "curl -v --form input=@{} --form consolidateCitations=1 {}:8070/api/processFulltextDocument".format(paper_path, server)
        xml = subprocess.check_output(command, shell=True)
        return (paper_path.split('/')[-1].split('.')[0], xml)
    except:
        pass
    return [0]



if __name__ == '__main__':



    PaperList = []
    for filename in glob.iglob('/home/rashedka/Desktop/halfOfPaper/dir_000/*.pdf', recursive=True):
        PaperList.append(filename)

    PaperList = set(PaperList)

    # processed_papers =  set([item.split(".")[0] for item in os.listdir("XMLFiles/")])
    # PaperList = PaperList - processed_papers
    N = len(PaperList)
    text_dic = {}
    worker_pool = Pool(40)
    for result in tqdm.tqdm(worker_pool.imap_unordered(extract_xml, PaperList), total=N):
        if len(result) > 1:
            outfile = open("XMLFiles/{}.xml" .format(result[0]), "wb")
            outfile.write(result[1])
            outfile.close()
            # print("herehre............................")
