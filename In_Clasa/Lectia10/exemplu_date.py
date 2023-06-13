
from tools import *
from args import create_args

args = create_args()

if args.flow == 'harvest':
   if args.timeout < 60:
       raise ValueError(
           f'Timeout este minim 60, ai introdus {args.timeout}'
       )
   harvest(args.timeout)
elif args.flow == 'exchange':
    exchange(args.target, args.amount)

    

#  .csv / coma separate values / var1,var2,var3 (excel)