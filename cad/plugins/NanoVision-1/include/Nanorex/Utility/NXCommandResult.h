// Copyright 2008 Nanorex, Inc.  See LICENSE file for details.

#ifndef NX_COMMANDRESULT_H
#define NX_COMMANDRESULT_H

#ifdef WIN32
#	ifdef _MSC_VER
#		pragma warning(disable:4786)
#	endif
#endif

#include <vector>
#include <QString>

namespace Nanorex {


/* CLASS: NXCommandResult */
/**
 * Encapsulates the results of a command execution.
 *
 * @see NXNanoVisionResultCodes
 * @ingroup NanorexUtility
 */
class NXCommandResult {
	public:
		NXCommandResult();
		void setResult(int resultId);
		int getResult();
		void setParamVector(std::vector<QString>& paramVector);
		const std::vector<QString>& getParamVector() const;

	private:
		int resultId;
		std::vector<QString> paramVector;
};

} // Nanorex::

#endif
