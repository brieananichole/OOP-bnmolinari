import java.util.ArrayList;

public class CakeMenu { //the cake menu is stored as an arraylist
    ArrayList<MenuItem> menuItems;

    public CakeMenu() {
        menuItems = new ArrayList<MenuItem>();
        
        addItem("Red Velvet Dream", "3 tiers of  our red velvet cake put together with french vanilla buttercream and topped with  dark chocolate ganache", 
        false, 24.99);

        addItem("Birthday Cake Bash", "2 layers of vanilla cake with rainbow sprinkles baked throughout, vanilla buttercream topped with more rainbow sprinkles and rainbow icing",
        true, 14.99);

        addItem("Carrot Cake Delight", "2 layers of our fan favorite carrot cake, smothered with pecan buttercream and topped with fresh pecans",
        true, 17.99);
    }

    public void addItem(String name, String description, boolean gF, double price)
    {
        MenuItem menuItem = new MenuItem(name, description, gF, price); //creates new item
        menuItems.addItem(menuItems); //adds new item to arraylist of menu items
    }

    public ArrayList<MenuItem> getMenuItems()
    {
        return menuItems;
    }

    public Iterator createIterator() 
    {
        return new CakeMenuIterator(menuItems);
    }

    public String toString()
    {
        return "Betty's Cake Menu";
    }
}