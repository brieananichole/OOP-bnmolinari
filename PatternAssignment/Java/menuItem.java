public class MenuItem {
    String name;
    String description;
    boolean gF;
    double price;

    public MenuItem (String name, String description, boolean gF, double price) //constructor
    {
        this.name = name;
        this.description = description;
        this.gF = gF;
        this.price = price;
    }

    public String getName ()
    {
        return name;
    }

    public String getDescription()
    {
        return description;
    }

    public boolean getgF()
    {
        return gF;
    }

    public double getPrice()
    {
        return price;
    }

    public String toString()
    {
        return (name + ", $" + price + "\n " + description);
    }
}

