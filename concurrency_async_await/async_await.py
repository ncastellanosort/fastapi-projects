'''

asynchronous code and paralellism

a way to tell the computer that he will wait for something to finish somewhere else.
during that time the computer can do other things.

it's called asynchronous because the computer / program
doesn;t have to be synchronized with the slow task.

the await means 'espere a'

'''

async def get_burgers(number: int):
   # Do some asynchronous stuff to create the burgers
   burgers = await get_burgers(2)
   return burgers

'''

the key here is the await. It tells Python that it has to wait ⏸ for get_burgers(2) to finish doing its thing 🕙 before storing the results in burgers. With that, Python will know that it can go and do something else 🔀 ⏯ in the meanwhile (like receiving another request).

'''