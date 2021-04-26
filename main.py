# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1: Greet template

def greet(name, template='Hello, <name>!'):

    greeting_template = template.replace('<name>', name)

    return greeting_template
    
# Part 2: force

def force(mass, body='earth'):
    planet_gravity={
        'sun':  274,
        'jupiter':  25.9,
        'neptune':  11.2,
        'saturn':  10.4,
        'earth':  9.8,
        'uranus':  8.9,
        'venus':  8.9,
        'mars':  3.7,
        'mercury':  3.7,
        'moon':  1.6,
        'pluto':  0.6
        }
    calculate_force = mass * planet_gravity[body]
    
    return calculate_force

#Part 3: Gravity

def pull(m1, m2, d,):
    
    g = 6.674e-11

    calculate_pul = g * ((m1 * m2) / (d * d))

    return calculate_pul





    
   

    
    


