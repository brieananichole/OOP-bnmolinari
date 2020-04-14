package iteratormenu;

public class Employee {
    Menu cakeMenu;
    Menu cookieMenu;

    public Employee(Menu cakeMenu, Menu cookieMenu) 
    {
        this.cakeMenu = cakeMenu;
        this.cookieMenu = cookieMenu;
    }

    public void printMenu() 
    {
        Iterator cakeIterator = cakeMenu.createIterator();
        Iterator cookieIterator = cookieMenu.createIterator();
        
        System.out.println("MENU\n----\nCAKES");
        printMenu(cakeIterator);
        System.out.println("\nCOOKIES");
        printMenu(cookieIterator);
    }

    private void printMenu(Iterator iterator)
    {
        while(iterator.hasNext()) {
            MenuItem menuItem = iterator.next();
            System.out.print(menuItem.getName()+ ", ");
            System.out.print(menuItem.getPrice()+ " -- ");
            System.out.print(menuItem.getDescription());
        }
    }

    public void printGlutenFreeMenu() {
        printGlutenFreeMenu(cakeMenu.createIterator);
        printGlutenFreeMenu(cookieMenu.createIterator);
    }

    public boolean isItemGlutenFree(String name)
    {
        Iterator cakeIterator = cakeMenu.createIterator();
        if(isGlutenFree(name, cakeIterator)) 
        {
            return true;
        }

        Iterator cookierIterator = cookieMenu.createIterator();
        if(isGlutenFree(name, cookieIterator))
        {
            return true;
        }

        return false;
    }

    public void printGlutenFreeMenu(Iterator iterator)
    {
        while(iterator.hasNext())
        {
            MenuItem menuItem = iterator.next();
            if (menuItem.isGlutenFree())
            {
                System.out.print(menuItem.getName());
                System.out.println("\t\t" + menuItem.getPrice())
                System.out.println("\t" +menuItem.getDescription());
            }
        }
    }

    private boolean isGlutenFree(String name, Iterator iterator) 
    {
        while (iterator.hasNext())
        {
            MenuItem menuItem = iterator.next();
            if (menuItem.getName().equals(name))
            {
                if (menuItem.isGlutenFree())
                {
                    return true;
                }
            }
        }
        return false;
    }
}
