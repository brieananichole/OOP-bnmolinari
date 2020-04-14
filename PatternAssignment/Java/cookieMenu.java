package iteratormenu;

public class CookieMenu implements Menu { //the cookie menu uses an Array
    static final int MAX_ITEMS = 10;
    int numOfItems = 0;
    MenuItem[] menuItems;


public CookieMenu()
{
    menuItems = new MenuItem[MAX_ITEMS];

    addItem("Cinnamon Oatmeal Swirl", "Our famous  giant oatmeal 
    cookie infused with a cinnamon roll style swirl", true, 2.99);

    addItem("Dark Chocolate Chunk", "Soft chocolate cookie with 
    chunky bits of dark chocolate", false, 1.99);

    addItem("Summer Day", "Chewy vanilla sugar cookie topped
    with lemon icing", false, 1.99);
}

public void addItem(String name, String description, boolean gF, double price)
{
    MenuItem menuItem = new MenuItem(name, description, gF, price);
    if (numOfItems >= MAX_ITEMS) {
        System.err.println("Sorry! Menu is full! Unable to add item to menu!");
    }
    else {
        menuItems[numOfItems] = menuItem;
        numOfItems = numOfItems + 1;    
    }
} 

public MenuItem[] getMenuItems() 
{
    return menuItems;
}

public Iterator createIterator() 
{
    return new CookieMenuIterator(menuItems);
}

}