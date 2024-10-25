
import template_1 from "../Images/sample_1.png";
import template_2 from "../Images/sample_2.png";
import template_3 from "../Images/sample_3.png";
import template_4 from "../Images/sample_4.png";



import Template1 from "../Templates/Template4";
import Template2 from "../Templates/Template3";

import Template3 from "../Templates/Template2";
import Template4 from "../Templates/Template1";


export const templates = [
  {
    id: 1,
    template_name: "Template-1",
    template_img: template_1,
    template: <Template1 />,
  },
  {
    id: 2,
    template_name: "Template-2",
    template_img: template_2,
    template: <Template2 />,
  },
  {
    id: 3,
    template_name: "Template-3",
    template_img: template_3,
    template: <Template3 />,
  },
  {
    id: 4,
    template_name: "Template-4",
    template_img: template_4,
    template: <Template4 />,
  },

];
