class QueryNode
{
public:
    QueryNode(const string& nodename, double vertex, QueryNode* prev): _nodename(nodename), _vertex(vertex), _prev(prev)
    {
    }
    string _nodename;
    double _vertex;
    QueryNode* _prev;
};

class Solution
{
public:
    double calcEquationForOne(map<string, map<string, double> >& graph, const string& startnode, const string& endnode)
    {
        set<string> visited;
        visited.insert(startnode);
        stack<QueryNode*> openstack;
        QueryNode* current = new QueryNode(startnode, 1, NULL);
        openstack.push(current);
        while (!openstack.empty())
        {
            current = openstack.top();
            if (current->_nodename.compare(endnode) == 0)
            {
                break;
            }
            openstack.pop();
            map<string, double>& neibors = graph[current->_nodename];
            for (map<string, double>::iterator it = neibors.begin();it != neibors.end(); ++it)
            {
                if (visited.find(it->first) == visited.end())
                {
                    visited.insert(it->first);
                    QueryNode* neibor = new QueryNode(it->first, it->second, current);
                    openstack.push(neibor);
                }
            }
            current = NULL;
        }
        if (!current)
        {
            return -1.0;
        }
        double answer = 1.0;
        while (current)
        {
            answer *= current->_vertex;
            current = current->_prev;
        }

        while (!openstack.empty())
        {
            current = openstack.top();
            openstack.pop();
            delete current;
        }
        return answer;
    }

    vector<double> calcEquation(
        vector<pair<string, string> > equations, 
        vector<double>& values, 
        vector<pair<string, string> > queries)
    {    
        vector<double> answers;
        map<string, map<string, double> > graph;
        vector<pair<string, string> >::iterator eit = equations.begin();
        vector<double>::iterator vit = values.begin();
        while (eit != equations.end() && vit != values.end())
        {
            graph[eit->first][eit->second] = *vit;
            graph[eit->second][eit->first] = 1.0 / (*vit);
            ++eit, ++vit;
        }
        for (vector<pair<string, string> >::iterator qit = queries.begin();qit != queries.end(); ++qit)
        {
            double answer;
            if (graph.find(qit->first) == graph.end() || graph.find(qit->second) == graph.end())
            {
                answer = -1.0;
            }
            else if (qit->first.compare(qit->second) == 0)
            {
                answer = 1.0;
            }
            else
            {
                answer = calcEquationForOne(graph, qit->first, qit->second);
            }
            answers.push_back(answer);
        }
        return answers;
    }
};
