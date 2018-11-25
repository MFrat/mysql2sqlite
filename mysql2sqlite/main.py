from context import Context
from process.generate_dump import Process

process = Process(Context.clone('dev'))
process.exec_dump()
print(process.dump)

