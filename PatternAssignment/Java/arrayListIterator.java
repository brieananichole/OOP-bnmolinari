import java.util.ArrayList;

public class ArrayListIterator implements iterator {
    ArrayList<MenuItem> items;
    int postion = 0;

    public ArrayListIterator(ArrayList<MenuItem> items)
    {
        this.items = items;
    }

    public MenuItem next()
    {
        MenuItem item = items.get(position);
        positon = positon + 1;
        return item;
    }

    public boolean hasNext()
    {
        if (postion >= items.size())
        {
            return false;
        }
        else
        {
            return true;
        }
    }
}
