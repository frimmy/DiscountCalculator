from optparse import OptionParser
from sys import exit

def determine_discount(cart_total, value, option):
	while True:
		if option.capitalize().strip() == 'Percent':
			return cart_total*((value)/100)
		elif option.capitalize().strip() == 'Value':
			return value
		elif option.capitalize().strip() == 'Q':
			exit()
		else:
			print "You didn't enter correct discount type. Please try again or enter 'q' to quit"
			option = raw_input("Enter 'percent' or 'value'> ")
# def calculate_discount(cart_total, discount, option):
#     """
#     Calculates dollar amount of discount off cart total
#     """
#     discount_ = calculate_discount(discount, option)
#     discount_value = dict(meal_base=meal_base,
#                     tax_rate=tax_rate,
#                     tip_rate=tip_rate,
#                     tax_value=tax_value,
#                     total = total)
#     return meal_info
 
 
def main():
    parser = OptionParser()
    parser.add_option("-c", "--cart", dest="cart", type="float", help="total shopping cart value")
    parser.add_option("-t", "--type", dest="percent_or_value", type="string", help="method of applying discount (either percentage or value)", default="percent" )
    parser.add_option("-d", "--discount", dest="discount", type="float", 
                        help="amount discount to be applied to cart")  
                        #let's accrue good karma by defaulting to a decent 20%
                        #tip!
    (options, args) = parser.parse_args()
    if not options.cart:
        parser.error("You forgot to indicate whether your discount is a percent or value!")
    if not options.percent_or_value:
        parser.error("You forgot to indicate the tax rate!")

    discount = determine_discount(options.cart, options.discount, 
                                    options.percent_or_value)
 
    print "The discount off your shopping cart is ${0:.2f}.".format(discount)
    # print "You need to pay ${0:.2f} for tax.".format(meal_info['tax_value'])
    # print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip.".format(
    #                                     int(100*meal_info['tip_rate']), 
    #                                     meal_info['tax_value'])
    # print "The grand total of your meal is ${0:.2f}.".format(meal_info['total'])
 
if __name__ == '__main__':
    main()