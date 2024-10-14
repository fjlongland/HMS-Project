import 'package:flutter/material.dart';
import 'package:hms_app/pages/submit.dart';

class ViewAssignments extends StatelessWidget {
  const ViewAssignments({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final List<String> assignments = [
      "EG1",
      "EG2",
      "EG3",
    ];

    return Scaffold(
        appBar: AppBar(
          title: const Text(
            'HMS',
            style: TextStyle(
                color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
          ),
          backgroundColor: Colors.white,
          elevation: 0.0,
          centerTitle: true,
        ),
        body: Padding(
            padding: const EdgeInsets.all(16.0),
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              const Text("Assignments",
                  style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Colors.black)),
              const SizedBox(height: 24.0),
              Expanded(
                  child: ListView.builder(
                      itemCount: assignments.length,
                      itemBuilder: (context, index) {
                        return Card(
                          margin: const EdgeInsets.symmetric(vertical: 8.0),
                          child: ListTile(
                            title: Text(assignments[index]),
                            onTap: () {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (context) =>
                                          const Submission()));
                            },
                          ),
                        );
                      }))
            ])));
  }
}
