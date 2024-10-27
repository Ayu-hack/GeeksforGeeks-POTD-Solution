class Solution
{
public:
    int countNodesinLoop(Node *head)
    {
        if (!head || !head->next)
            return 0;

        Node *s = head;
        Node *f = head;
        while (f && f->next)
        {
            s = s->next;

            f = f->next->next;

            if (s == f)
            {
                int l = 1;

                Node *current = s;

                while (current->next != s)
                {
                    current = current->next;

                    l++;
                }

                return l;
            }
        }

        return 0;
    }
};