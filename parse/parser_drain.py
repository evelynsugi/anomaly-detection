import sys
from logparser import Drain #parser: Drain

input_dir = "raw_data/"
output_dir = "parsed_data/drain/"
HDFS_data = "HDFS.log"
HDFS_data_trainset = "HDFS_trainset.log"
HDFS_data_testset = "HDFS_testset.log"
log_format = "<Date> <Time> <Pid> <Level> <Component>: <Content>"

regex = [
    r"blk_(|-)[0-9]+",
    r"(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)",
    r"(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$",
]
st = 0.5
depth = 4

# parse the whole trainset
parser = Drain.LogParser(
    log_format, indir=input_dir, outdir=output_dir, depth=depth, st=st, rex=regex
)
parser.parse(HDFS_data)


# parse the trainset
parser = Drain.LogParser(
    log_format, indir=input_dir, outdir=output_dir, depth=depth, st=st, rex=regex
)
parser.parse(HDFS_data_trainset)

# parse the testset
parser = Drain.LogParser(
    log_format, indir=input_dir, outdir=output_dir, depth=depth, st=st, rex=regex
)
parser.parse(HDFS_data_testset)