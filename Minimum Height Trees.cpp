class Solution {
public:
    bool deleteFromGraph(map<int, set<int> > &graph, int node) {
        map<int, set<int> >::iterator it = graph.find(node);
        if (it != graph.end() && it->second.size() == 1) {
            for (set<int>::iterator it2 = it->second.begin();it2 != it->second.end(); ++it2) {
                map<int, set<int> >::iterator it3 = graph.find(*it2);
                set<int>::iterator it4 = it3->second.find(it->first);
                it3->second.erase(it4);
            }
            graph.erase(it);
            return true;
        }
        return false;
    }
    void allLeafInGraph(map<int, set<int> > &graph, vector<int> &leaves) {
        map<int, set<int> >::iterator it;
        for (it = graph.begin();it != graph.end(); ++it) {
            if (it->second.size() == 1) {
                leaves.push_back(it->first);
            }
        }
    }
    vector<int> findMinHeightTrees(int n, vector<pair<int, int> >& edges) {
        map<int, set<int> > graph;
        vector<int> answer;
        for (int i = 0;i < n; ++i) {
            set<int> hisset;
            graph[i] = hisset;
        }
        for (vector<pair<int, int> >::iterator it = edges.begin();it != edges.end(); ++it) {
            int node1 = it->first, node2 = it->second;
            graph[node1].insert(node2);
            graph[node2].insert(node1);
        }
        //read map OK
        int totalNum = n;
        while (totalNum > 2) {
            vector<int> leaves;
            allLeafInGraph(graph, leaves);
            for (vector<int>::iterator lit = leaves.begin();lit != leaves.end(); ++lit) {
                if (deleteFromGraph(graph, *lit)) {
                    --totalNum;
                }
            }
        }
        for (map<int, set<int> >::iterator it = graph.begin();it != graph.end(); ++it) {
            answer.push_back(it->first);
        }
        return answer;
    }
};